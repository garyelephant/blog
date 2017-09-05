## 大数据技术栈

大数据技术栈：Zookeeper, Hdfs, Yarn, Spark, HBase, Hive, Presto, Elasticsearch, Kafka, Redis, Flume, Logstash，mapd,neo4j，mysql，mongodb，文件格式（Parquet, Carbondata, Lucene, Arrow）

大数据与分布式系统重要理论：CAP, MapReduce, MPP, Paxos, 2PC, 3PC，MVCC

架构知识：数据仓库，流式计算，多维查询，搜索，日志收集，OLAP，OLTP，分布式锁和主从选举, Lambda

设计模式：

数据结构与算法：排序、树、图基础算法，红黑树，BTree, skipList, HashMap, LinkedHashMap, 大数据算法

并发模型：actor, reactor, I/O多路复用（I/O Multiplexing）机制(select, epoll)

编程语言：Java, Scala, Python

纬度划分：计算，存储，网络

---

## 基础：计算

cgroups

## 基础：存储

Raid

## 基础：网络

SDN

VLAN: http://network.51cto.com/art/201409/450885_all.htm

## 编程语言

### Java

JVM进程、线程模型

线程同步和线程安全（重点ExecutorService, Future）

jdk常用数据结构的实现方式(重点ArrayList, LinkedList, HashMap, ConcurrentHashMap)

GC原理及调优

Java高并发程序的实现方法

反射和依赖注入

Java8 Stream 并行计算实现的原理
http://lvheyang.com/?p=87

如何实现无锁的链表(CAS)


### Python

Python并发模型，GIL

GC原理及调优

常用数据结构的实现方式

### Scala

Q1: class vs object vs trait vs case class?

## 数据结构与算法

排序算法

SkipList

树的数据结构与常用算法（重点红黑树、BTree）

图的数据结构与常用算法

HashMap, LinkedHashMap

大数据算法

详见[数据结构与算法笔记](./data-structure-algorithms.md)

## 设计模式

常用设计模式

如何用java，python实现常用设计模式

## 架构知识

数据仓库，流式计算，多维查询，搜索，日志收集，OLAP，OLTP，分布式锁和主从选举

## 大数据与分布式系统重要理论

CAP, MapReduce, MPP, Paxos, 2PC, 3PC，MVCC, WAL(Write ahead log)

## 大数据技术栈

> 待定：mapd,neo4j

> 数据库：mysql，mongodb

Q1: MySQL 不同引擎的区别？

Q2: MySQL, Mongodb 索引的原理？

A2: 详见[MySQL索引背后的数据结构及算法原理](http://blog.codinglabs.org/articles/theory-of-mysql-index.html)

```
B+树的实现细节是什么样的？B-树和B+树有什么区别？联合索引在B+树中如何存储？

索引原理，分不同的存储引擎：

(1) MyISAM的索引文件仅仅保存数据记录的地址。在MyISAM中，主索引和辅助索引（Secondary key）在结构上没有任何区别，只是主索引要求key是唯一的，而辅助索引的key可以重复

(2) InnoDB的数据文件本身就是索引文件,叶节点包含了完整的数据记录。这种索引叫做聚集索引。因为InnoDB的数据文件本身要按主键聚集，
所以InnoDB要求表必须有主键（MyISAM可以没有），如果没有显式指定，则MySQL系统会自动选择一个可以唯一标识数据记录的列作为主键，
如果不存在这种列，则MySQL自动为InnoDB表生成一个隐含字段作为主键，这个字段长度为6个字节，类型为长整形。
InnoDB的辅助索引data域存储相应记录主键的值而不是地址。换句话说，InnoDB的所有辅助索引都引用主键作为data域。
```

Q3: MySQL中，什么样的查询会用到索引？

Q4: 为什么Mysql用的是B+tree, Mongodb用的是B-tree, Lucene用的是SkipList ?

Q5: MySQL, Mongodb 如何实现HA ?

> 数据传输：Flume, Logstash

> 消息队列：Kafka

> 搜索，多维分析：Elasticsearch

> 数据仓库：Hive

> 文件格式：Parquet, Carbondata, Lucene, Arrow, mmdb

Q1: 画出完整的Parquet文件格式?

Q2: 画出完整的Lucene文件格式?

文件格式相关的笔记见[列式存储文件笔记](./bigdata_fileformat.md)

> 计算：Spark

Q1: RDD是什么？

A1: RDD是分布式的数据集。RDD划分成多个Partition分布到集群中，分区的多少涉及对这个RDD进行并行计算的粒度。RDD依赖关系，分两种：窄依赖(Narrow Dependencies)和宽依赖(Wide Dependencies)。
窄依赖是指每个父RDD都之多被一个RDD的分区使用，而宽依赖是多个子RDD的分区依赖一个父RDD的分区。例如map，filter操作是窄依赖，而join，groupbykey是宽依赖。

Q2: 任务的调度？如何做容错（失败的任务和执行慢的任务）？

A2: 计算与数据就近原则。在作业中如果某个任务执行缓慢，系统会在其他节点上执行该任务的副本，与MapReduce推测执行做法类似，取最先得到的结果作为最终的结果。

Job中的Stage是通过DAGScheduler划分的，一次shuffle（宽依赖）划分2个stage，

Q3: 什么是DAG ? 

Q4: Job/Stage/Task的并行执行关系？

一个Action生成一个Job，一次shuffle划分2个stage，task根据RDD Partition 一一对应生成。

同一个Job中的不同Stage不能并行，同一个Stage中的不同Task可以并行。Task是执行的最小单元。

Q5: Spark vs MapReduce

A5: 内存迭代计算，任务依赖关系用DAG表示，支持map，reduce以外更丰富的算子。

Q6: Spark 如何做存储（内存/磁盘）管理？

Q7: Spark SQL 长短作业的公平调度？

Q8: Shuffle 原理和优化？

Q9: Spark Join 优化?

A9: https://www.slideshare.net/databricks/optimizing-apache-spark-sql-joins

Q10: 如何存储和调度非常大（内存不够）的RDD？

Q11: Spark 消息通信原理？

A11: (1) Spark 运行时消息通信：用户提交应用程序时，应用程序的SparkContext会向Master发送应用注册消息，并由Master给该应用分配Executor,
Executor启动后，Executor会向SparkContext发送注册成功消息；当SparkContext的RDD触发action操作后，将创建RDD的DAG，通过DAGScheduler划分Stage,
并将Stage转化为TaskSet;接着由TaskScheduler向注册的Executor发送执行消息，Executor接收到任务消息后启动并运行；最后当所有任务运行完，
由Driver处理结果并回收资源。

Q12: Spark代码中，哪部分是在Driver端执行的？哪部分是在Executor端执行的？

Q13: RDD vs DataFrame vs DataSet ?

A13: 底层计算优化(catalyst)：结构化的数据计算，DataFrame/DataSet比RDD高很多。类型安全

Q14: Spark SQL 原理（执行流程，逻辑计划，物理计划，优化器）？

Catalyst优化：优化处理查询语句的整个过程，包括解析、绑定、优化、物理计划等，主要由关系代数（relation algebra）、表达式（expression）以及查询优化（query optimization）组成。

Q15: Spark如何支持exactly-once的数据处理？

输入时记录offset, 输出时，确保是幂等或者支持事务。

幂等：输出多次，结果相同，比如生成文件覆盖上次生成的文件。

> 计算：Presto

> NoSQL: HBase

> 资源管理调度：Yarn(资源隔离方法，调度策略，HA)

Q1: Yarn各节点的角色及功能？

Q2: Yarn如何做资源隔离？

Q3: Yarn如何做资源调度，有哪些调度算法？

Q4: Yarn如何做HA?

> 存储：HDFS(namenode HA, fsimage)

Q1: Hdfs各节点的角色及功能？

Q2: Hdfs File的文件组成？

Q3: Hdfs 文件读写的交互流程？

Q4: HDFS 如何做HA?

https://www.ibm.com/developerworks/cn/opensource/os-cn-hadoop-name-node/

Q5: Hdfs文件block的放置策略？

A5: 相同rack 2个，其他rack 1个

Q6: Rack 感知？

A6: 在core-site.xml中配置`net.topology.script.file.name`，指定rack感知脚本.

> 分布式一致性：Zookeeper，分布式锁和主从选举
