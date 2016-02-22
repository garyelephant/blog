# 生产环境中应用Mesos前应该清楚的几个问题

---

> Mesos 能够管理每台机器的 CPU，内存等资源，让你像操纵单个资源池一样来操纵整个数据中心。

### 我们是否真的需要Mesos ?

我们遇到哪些问题，mesos给我们哪些好处？我们要作出哪些牺牲？

### Mesos能分配、隔离哪些资源？

资源隔离方式

### 资源是怎么分配的？

资源分配策略和算法

### Mesos是如何实现资源更合理应用的？

见这张图：

![resource utilization](http://cdn3.infoqstatic.com/statics_s1_20160120-0059/resource/articles/analyse-mesos-part-02/zh/resources/mesos-elastic-cea4da90b3c819bd96b3158da1a6f86b.jpg)

### Mesos如何实现更加合理高效的运维的？

### Mesos上面能跑有状态服务吗？

elasticsearch, hdfs, kafka, cassandra

### 想在生产环境用好Mesos，需要哪些技术？

mesos + marathon + docker + Service Discovery + load balancing

### 怎样才能做好服务自动failover, falut tolerant

http://mesosphere.github.io/presentations/apachecon-2015/containers/#/35

### Yarn vs Mesos

### 其他问题？

*	不同服务的端口冲突
*	对于需要做系统调优的服务怎么办？
*	对于需要使用filesystem cache的服务
*	不同的存储型服务同时使用同一块磁盘，对性能影响多大

### 实践建议

*	优先上线无状态、不需要服务发现、各个实例单独运行的应用（如Logstash, Kibana）

*	有状态的服务需要逐个验证，慢慢来。现在开源社区里的Framework还不是production ready, 如elasticsearch on mesos. 对于现在常见的分布式存储系统如hdfs, kafka, cassandra, elasticsearch，有状态服务的伸缩需要服务层面的支持。如增加一个es节点，需要迁移部分数据。减少es节点需要先将这些节点上的数据迁移走。如果直接下线，如对于shard=1, replica=0并且存储在此节点上的Index,数据会全部丢失；如果直接下线多个节点也有可能导致数据丢失和recovery时带来的大量网络、磁盘IO开销，降低服务质量。所以有状态服务的“自由”伸缩其实并不像无状态服务那样“自由”。

*	mesos 还是要和docker结合在一起（因为没有docker, mesos还不能实现统一的、隔离的环境）

*	如果你是做大数据服务的，服务核心围绕hadoop技术栈展开，还是用yarn更合适。Mesos和Yarn的服务层次决定了用Mesos完全代替Yarn绝不是理性的，很可能还要搞Yarn on Mesos

*	但是如果你的服务器资源规模大，应用种类多，运行实例多，或者说你们是公司里的平台架构部、云计算部门，用Mesos就很适合，也符合 Mesos 分布式操作系统内核的理念，可以构建一个Google 那样的Paas。

---

> Written with [StackEdit](https://stackedit.io/).