# Zookeeper 关键技术点

## 关键技术点

---

## FAQ

1. Zookeeper 有几种类型的Node ?

* PERSISTENT

* EPHEMERAL

* SEQUENCE

2. 什么是 Ephemeral Node ？

```
(Ephemeral Node)临时节点驻存在ZooKeeper中，当连接和session断掉时被删除。这个特性可以用来做应用的Master选举和服务发现。

比如通过ZooKeeper发布服务，服务启动时将自己的信息注册为临时节点，当服务断掉时ZooKeeper将此临时节点删除，这样client就不会得到服务的信息了。
```

3. 如何利用zookeeper来实现应用的Master选举并保证集群Master可用性和唯一性？zookeeper竞选Master包含哪些过程？zookeeper竞选Master机制利用了zk哪些特性？

在确保zookeeper集群节点安装配置的前提下，假设zk已经对外提供了正常的服务，通过下面的步骤来实现Master竞选：

* Step1: Client连接到zk上，判断znode /Roles/workers是否存在，不存在则建立，znode的类型是PERSISTENT类型，
保证不会随着C1的session断开而消失。

* Step2: Client在/Roles/workers下面建立一个SEQUENCE|EPHEMERAL类型的znode，前缀可以是worker，由zk保证znode编号是递增而且是暂时的，
EPHEMERAL在前文说了，一旦session断开创建的znode也会消失。

* Step3: Client通过getChildren获取所有的/Roles/workers下znode列表，并且设置一个Watcher等待通知，
返回值有多少个znode数量就对应Client来竞选。

* Step4: 对于步骤4返回的节点列表进行排序，找到最小的worker编号，如果是和自己创建的一致（步骤2返回值），那么就代表自己的编号是最小的，
自己就是Master。如果发现自己的编号不是最小，那么就等待通知，一旦Watcher触发，就在Watcher回到步骤3。

上面的机制主要利用了zk的几个特性

* 对于N个客户端同时请求create一个znode，zk能保证顺序的一致性，并且保证每个客户端创建的znode节点是递增并且唯一。

* 因为创建的znode是临时的，一旦session断开，那么znode就会从zk上消失，从而给每个设置Watcher的客户端发送通知，
让每个客户端重新竞选Master，编号小的肯定是Master，保证了唯一性。

TODO: 选主有两种方式？简单的判断Ephemeral node存活和这里介绍的方式，哪个更好？

参考 [zookeeper适用场景：如何竞选Master及代码实现](http://www.cnblogs.com/likehua/p/4060301.html)


4. 如何Failover, 如何选主？

5. Zookeeper如何保证数据一致性? 

6. 如何基于Zookeeper 开发分布式程序的分布式锁、主从选举、成员管理？

--

## References

1. 用zookeeper实现简单的master选举 http://blog.csdn.net/qq_32523587/article/details/62226611

2. ZooKeeper 选主流程: http://blog.csdn.net/liuyuehu/article/details/52136945

3. zookeeper的选主流程(源码分析) http://blog.csdn.net/qinghua9/article/details/22858033

4. 《从Paxos到Zookeeper : 分布式一致性原理与实践》