## Hadoop(HDFS, Yarn)关键技术点整理

TODO:

* Scheduler/Queue http://www.corejavaguru.com/bigdata/hadoop-tutorial/yarn-scheduler
* Cgroup
* ResourceManager High Availability
* YARN Node Labels
* The YARN Timeline Server


### 1. HDFS

* HDFS架构简介：https://hadoop.apache.org/docs/r2.7.0/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html
 
* HDFS各个角色的作用：
  **NameNode**
维护着文件系统树(filesystem tree)以及文件 树中所有inode的(文件和文件夹)的元数据(metadata)。对于文件来说包括了数据块描述信息、修改时间、访问时间等；对于目录来说包括修改时间、访问权限控制信息(目录所属用户，所在组)等。
 **DataNode**
管理本地存储，响应客户端的读写请求，在namenode的指导下进行块的创建，删除，复制。
 **ZKFC(可选)**
当需要NameNode HA自动Failover时必选。用于管理NameNode状态。主要包括以下三个功能：Health monitoring，ZooKeeper session management，ZooKeeper-based election
详细介绍：https://hadoop.apache.org/docs/r2.7.0/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithQJM.html#Automatic_Failover
 **JournalNode(可选)**
 当需要NameNode HA时必选。两个NameNode为了保持数据一致需要通过JournalNode通信。最多允许 (N - 1) / 2个节点失败，所以建议部署奇数个实例。Active的namenode修改元数据时会持久化一条记录到JournalNodes的master节点。Standby的Namenode会监听这些变化并应用到自己的元数据上。
 
* HDFS + yarn 部署流程
 (1) 修改主机名
 (2) 配置SSH免密码登录
 (3) 安装JRE
 (4) 下载Hadoop发布版，解压缩到服务器
 (5) 配置core-site.xml，hdfs-site.xml,slaves
 (6) NameNode格式化
 (7) 启动 ./sbin/start-dfs.sh
 (8) 配置mapred-site.xml，yarn-site.xml
 (9) 启动 ./sbin/start-yarn.sh
 
* HA HDFS 部署流程（将一个非HA的集群转换为HA的集群）
 (1)在hdfs-site.xml中增加HA的相关配置（**dfs.nameservices**,**dfs.ha.namenodes.[nameservice ID]**,**dfs.namenode.rpc-address.[nameservice ID].[name node ID]**,**dfs.namenode.http-address.[nameservice ID].[name node ID]**,**dfs.namenode.shared.edits.dir**,**dfs.client.failover.proxy.provider.[nameservice ID]**,**dfs.ha.fencing.methods**，**dfs.journalnode.edits.dir**）
 (2)在 core-site.xml中增加相关配置（**fs.defaultFS**）
 (3)将Active的NameNode元数据的目录拷贝到StandBy的NameNode
 (4)执行`hdfs namenode -initializeSharedEdits`初始化JournalNodes
 `(5),(6)为自动Failover的配置`
 (5)在hdfs-site.xml中打开自动failover:
 dfs.ha.automatic-failover.enabled；
 配置zk地址:
 ha.zookeeper.quorum
 (6)初始化ZKFC
 /bin/hdfs zkfc -formatZK
 (7)启动HDFS:start-dfs.sh
 
* HDFS读写的流程 
**读:**Client向NameNode发送读请求，NameNode返回block列表，Client选择离最近的DataNode读取block，如果在读取的过程中失败，就尝试连接别的DataNode进行读取。
**写:**
(1)Client向NameNode发送写请求，Namenode检查目标文件是否已经存在，检查是否可以上传
(2)NameNode返回是否可以上传
(3)Client对文件进行切分，切分为Block，并请求NameNode上传第一个block
(4)namenode返回datanode的服务器
(5)Client请求一台datanode上传数据，构建pipeline，第一个datanode收到请求会继续调用第二个datanode，然后第二个调用第三个datanode，将整个pipeline建立完成，逐级返回客户端
(6)Client以packet为单位传输文件
(7)当一个block传输完成之后，client再次请求namenode上传第二个block的服务器 重复(4)-(6)

#### 1.5 HDFS HA

#### 1.6 写文件到HDFS如何保证数据一致性

场景Spark 生成Parquet 写入 HDFS， 如何保证数据一致性：

此场景利用了 Hadoop FileOutputCommitter 的 Rename 机制（Spark写文件还是调用Hadoop的相关库来完成的），

我们只是想把数据写入到S3某个路径下，为什么会出现先写到temporary目录，再Rename到真实目录的情况？

假设我们直接把数据写入到指定的路径下，会出现哪些问题？

* 由于是多个Task并行写文件，如何保证所有Task写的所有文件要么同时对外可见，要么同时不可见？在下图示例中，三个Task的写入速度是不同的，那就会导致不同时刻看到的文件个数是不一样的。另外，如果有一个Task执行失败了，就会导致有2个文件残留在这个路径下。

* 同一个Task可能因为Speculation或者其他极端原因导致某一时刻有多个Task Attempt同时执行，即同一个Task有多个实例同时写相同的数据到相同的文件中，势必会造成冲突。如何保证最终只有一个是成功的并且数据是正确的？

* 某个spark executor中的task在执行过程中，executor挂了，原来在这个executor上面的task会自动在其他executor上重新执行，如果这些task的工作是生成parquet文件，写入hdfs，那么是否会导致数据重复？

上述的问题都与数据一致性有关，为了应对这些问题，尽可能保证数据一致性，Hadoop FileOutputCommitter设计了Rename机制（Spark写文件还是调用Hadoop的相关库来完成的）。Rename机制先后有两个版本：v1和v2，二者在性能和保证数据一致性的粒度上有所区别。

Rename 机制有2个版本:

v1: 2次Rename, 步骤：(1) write _temporary dir for task in _temporary dir for job, (2) do `commitTask`, rename _temporary task dir (3) do `commitJob`, rename _temporary job dir (3) add `_SUCCESS` flag file

v2[牺牲一定的一致性，提高性能]: 1次Rename, (1) write _temporary dir for task in _temporary dir for job, (2) do `commitTask`, rename _temporary task dir[直接rename到最终目录] (3) add `_SUCCESS` flag file

来自: https://bruce.blog.csdn.net/article/details/87955023
 
### 2. YARN

* 提交任务的流程

(1) Client向RM发送New Application Request请求，RM返回ApplicationID
(2) Client构造并发送ApplicationSubmitContext(包括了调度队列，优先级，用户认证信息，ApplicationID，AM的ContainerLaunchContext(jar包、依赖文件、安全token、启动的shell脚本))
(3) RM在NodeManager上创建container，并启动AM
(4) AM向RM发起注册请求，RM返回集群资源情况
(5) AM向RM请求资源，传递的信息主要包含请求container的列表
(6) RM在收到AM的资源请求后，会根据调度策略，来分配container以满足AM的请求
(7) AM向container所在机器的NM发送ContainerLaunchContext来启动container

* Scheduler 

FIFO/Capacity/Fair Scheduler:

https://blog.csdn.net/zhanyuanlin/article/details/71516286

#### 2.3 YARN HA


---

## Yarn FAQ:

Q1: Yarn各节点的角色及功能？

Q2: Yarn上Application运行流程？

Q3: Yarn如何做资源隔离？

Q4: Vcore vs cores ?

Q5: Yarn如何做资源调度，有哪些调度算法, 如何配置？Yarn队列的作用？

可以分两层，第一小层是YARN的队列，第二小层是队列内的调度。Spark作业提交到不同的队列，通过设置不同队列的minishare、weight等，来实现不同作业调度的优先级，
这一点Spark应用跟其他跑在YARN上的应用并无二致，统一由YARN公平调度。比较好的做法是每个用户单独一个队列，这种配置FAIR调度就是针对用户的了，
可以防止恶意用户提交大量作业导致拖垮所有人的问题。这个配置在hadoop的yarn-site.xml里。

```
<property>
    <name>yarn.resourcemanager.scheduler.class</name>
    <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
</property>
```

---

## HDFS FAQ:

Q1: Hdfs各节点的角色及功能？

Q2: Hdfs File的文件结构？

Q3: Hdfs 文件读写的交互流程？

Q4: HDFS 如何做HA?

https://www.jianshu.com/p/3a6616630ad8

https://www.ibm.com/developerworks/cn/opensource/os-cn-hadoop-name-node/

https://www.cnblogs.com/dadadechengzi/p/6715906.html

https://www.cnblogs.com/juncaoit/p/6003172.html

Q5: Hdfs文件block的放置策略？

A5: 相同rack 2个，其他rack 1个

Q6: Rack 感知？

A6: 在core-site.xml中配置`net.topology.script.file.name`，指定rack感知脚本.

Q7: Hdfs Federation

https://blog.csdn.net/yinglish_/article/details/76785210


---

Hadoop 架构分析：

1. [Hadoop架构原理](http://mp.weixin.qq.com/s?__biz=MzU0OTk3ODQ3Ng==&mid=2247483809&idx=1&sn=a8d087c21171bf164fcda389ada9404a&chksm=fba6e9a2ccd160b4e1423c6d142b18849ded66cfdc1477e4d601e44f832d7026b64d80af8db1&mpshare=1&scene=24&srcid=#rd)

2. [大规模集群下Hadoop NameNode如何承载每秒上千次的高并发访问](http://mp.weixin.qq.com/s?__biz=MzU0OTk3ODQ3Ng==&mid=2247483821&idx=1&sn=872dad184dc230a1988973d3023eb837&chksm=fba6e9aeccd160b80a5c4c7957f045057bfff64bf5769eac976a2191d42511f14ff4cdabb5db&mpshare=1&scene=24&srcid=#rd)

3. [Hadoop如何将TB级大文件的上传性能优化上百倍？](http://mp.weixin.qq.com/s?__biz=MzU0OTk3ODQ3Ng==&mid=2247483830&idx=1&sn=ae6be8cf2f1361044de9577170afd887&chksm=fba6e9b5ccd160a3ca904630c2d634fbe5c302f6b5d8350de23eabbacd1f499c7d00bce47344&mpshare=1&scene=24&srcid=#rd)

4. [看Hadoop底层算法如何优雅的将大规模集群性能提升10倍以上？](http://mp.weixin.qq.com/s?__biz=MzU0OTk3ODQ3Ng==&mid=2247483900&idx=1&sn=f7d66378d68306ee3732e1e7ba60561a&chksm=fba6e9ffccd160e9cd1f9843e2abcb411c67adfcafbab1715401da1bedbf6a010e6821508057&mpshare=1&scene=24&srcid=#rd)

5. [大规模集群下的Hadoop高并发以及高性能架构原理总结](http://mp.weixin.qq.com/s?__biz=MzU0OTk3ODQ3Ng==&mid=2247483932&idx=1&sn=02849bfdb31d708df28a3f689b7a8ffc&chksm=fba6ea1fccd163096ba2fe2984444683308efb7b420e2174be225af4f709e47436dc63bc17dd&mpshare=1&scene=24&srcid=#rd)

---


