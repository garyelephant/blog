## 大数据面试求职考点大纲完备整理

> 本人目前在国内某一线互联网从事大数据架构工作，这些考点大纲和资料整理都是之前面试的经验整理。
> 如果有哪位同学，需要大数据求职面试辅导，请加微信 `garyelephant`。或者扫码加我微信：

<img src="../images/garyelephant.jpeg" height="180" width="180">

最后更新时间2020年2月14日。

---

* 基础知识
  * 数据结构与算法：排序、树、图基础算法，红黑树，BTree, skipList
  * 普通的技巧型面试题，参考《剑指offer》以及[在线题目](https://www.nowcoder.com/ta/coding-interviews?page=1)，《编程之美》，《编程珠玑》，《程序员代码面试指南—IT名企算法与数据结构题目最优解》, [leetcode](https://leetcode-cn.com/articles/)，[牛客网]()
  * 海量数据算法面试题 [link1](https://blog.csdn.net/wypersist/article/details/80114709), [link2](https://www.jianshu.com/p/f56ef7b23686), [Bloom Filter-1](https://www.cnblogs.com/zhxshseu/p/5289871.html), [Bloom Filter-2](https://www.jianshu.com/p/b0c0edf7686e)
  * 编程语言基础及核心知识：
    * Java, Scala (JVM, GC, ClassLoader, 反射，泛型, 注解，切面，ServiceLoader, CodeGeneration, Collections(HashMap, LinkedHashMap, TreeMap, ConcurrentHashMap, BlockingQueue), ThreadPool, concurrent库, NIO) 
    * Python(GIL, GC)
  * 并发模型：actor, reactor, I/O多路复用（I/O Multiplexing）机制(select, epoll)
  * 设计模式：
  
* 大数据技术栈(计算，存储，网络)：
 
  * Hdfs, 
  * Yarn, 
  * Spark(+ Spark MLlib), 
  * Kafka
  * Azkaban
  * Presto
  * Elasticsearch,
  * HBase,
  * Zookeeper, 
  * Hive, 
  * Flume, 
  * 文件格式（Parquet, Carbondata, Lucene, Arrow）
  
* 数据库技术
  * mysql（索引，事务，事务隔离级别，锁, 范式, binlog）
  * mongodb

* 大数据与分布式系统重要理论：参见[大数据关键理论的笔记](./bigdata-theory.md)
  * 分布式系统理论：CAP, MapReduce, DAG, MPP
  * 数据仓库理论, 数据仓库模型设计(分层建设、主题模型、元数据管理), 参见[数据仓库模型](./datawarehouse-theory.md)
  * OLAP，OLTP, Ad-hoc
  * 一致性协议：Paxos
  * 分布式事务: 2PC, 3PC，TCC
  * MVCC
  

* 架构知识：
  * 数据仓库，
  * 流式计算，
  * 多维查询，
  * 搜索，
  * 日志收集，
  * 分布式锁和主从选举, 
  * Lambda架构
  * 高可用
  * 数据治理、元数据管理、数据质量监控
  * 消息队列
  * 集群管理
  
参考《石衫的架构笔记》 
  
  
* `大数据 + 业务` 的应用案例
  * BI
  * 推荐
  * 用户画像
  * 审计/风控


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

参见[Java 关键技术点](./java.md)

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

参考[设计模式学习笔记](./design-patterns.md)

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

Q6: MySQL 的事务隔离级别？

[MySQL的四种事务隔离级别](https://www.cnblogs.com/huanongying/p/7021555.html)

[MySQL事务隔离级别的实现原理](https://www.cnblogs.com/cjsblog/p/8365921.html)

[MySQL的事务隔离级别](http://blog.itpub.net/31559358/viewspace-2221931/)

> 数据传输：Flume, Logstash

参考笔记：[每秒百万级流式日志处理架构的开发运维调优笔记](https://cloudblog.github.io/2016/11/19/%E6%AF%8F%E7%A7%92%E7%99%BE%E4%B8%87%E7%BA%A7%E6%B5%81%E5%BC%8F%E6%97%A5%E5%BF%97%E5%A4%84%E7%90%86%E6%9E%B6%E6%9E%84%E7%9A%84%E5%BC%80%E5%8F%91%E8%BF%90%E7%BB%B4%E8%B0%83%E4%BC%98%E7%AC%94%E8%AE%B0/)

> 消息队列：Kafka

参考笔记：[Kafka关键技术点](./kafka.md)

> 搜索，多维分析：Elasticsearch

参考笔记：[Elasticsearch关键技术点](./elasticsearch.md)

> 数据仓库：Hive

> 文件格式：Parquet, Carbondata, Lucene, Arrow, mmdb

Q1: 画出完整的Parquet文件格式?

Q2: 画出完整的Lucene文件格式?

文件格式相关的笔记见[列式存储文件笔记](./bigdata_fileformat.md)

> 计算：Spark

参考笔记 [Spark 关键技术点](./spark_notes.md)

> 计算：Presto

参考笔记 [Presto关键技术点](./presto.md)

> NoSQL: HBase

> 资源管理调度：Yarn(资源隔离方法，调度策略，HA)

Yarn与HDFS的笔记整理见[HDFS, Yarn关键技术点](./hdfs-yarn.md)

> 存储：HDFS(namenode HA, fsimage)

Yarn与HDFS的笔记整理见[HDFS, Yarn关键技术点](./hdfs-yarn.md)

> 分布式一致性：Zookeeper，分布式锁和主从选举

参考笔记：[Zookeeper关键技术点](./zookeeper.md)

---

> 本人目前在国内某一线互联网从事大数据架构工作，这些考点大纲和资料整理都是之前面试的经验整理。
> 如果有哪位同学，需要大数据求职面试辅导，请加微信 `garyelephant`。或者扫码加我微信：

<img src="../images/garyelephant.jpeg" height="180" width="180">
