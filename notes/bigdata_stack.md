## 大数据技术栈

大数据技术栈：Zookeeper, Hdfs, Yarn, Spark, HBase, Hive, Presto, Elasticsearch, Kafka, Redis, Flume, Logstash，mapd,neo4j，mysql，mongodb，文件格式（Parquet, Carbondata, Lucene, Arrow）

大数据与分布式系统重要理论：CAP, MapReduce, MPP, Paxos, 2PC, 3PC，MVCC

架构知识：数据仓库，流式计算，多维查询，搜索，日志收集，OLAP，OLTP，分布式锁和主从选举

设计模式：

数据结构与算法：排序、树、图基础算法，红黑树，BTree, skipList, HashMap, LinkedHashMap, 大数据算法

编程语言：Java, Python

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

jdk常用数据结构的实现方式

GC原理及调优

Java高并发程序的实现方法

反射和依赖注入

Java8 Stream 并行计算实现的原理
http://lvheyang.com/?p=87

### Python

Python并发模型，GIL

GC原理及调优

常用数据结构的实现方式

## 数据结构与算法

排序算法

树的数据结构与常用算法（重点红黑树、BTree, skipList）

图的数据结构与常用算法

HashMap, LinkedHashMap

大数据算法

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

Q3: MySQL, Mongodb 如何实现HA ?

> 数据传输：Flume, Logstash

> 消息队列：Kafka

> 搜索，多维分析：Elasticsearch

> 数据仓库：Hive

> 文件格式：Parquet, Carbondata, Lucene, Arrow, mmdb

Q1: 画出完整的Parquet文件格式?

Q2: 画出完整的Lucene文件格式?

> 计算：Spark

Q1: RDD是什么？

A1: RDD是分布式的数据集。RDD划分成多个Partition分布到集群中，分区的多少涉及对这个RDD进行并行计算的粒度。RDD依赖关系，分两种：窄依赖(Narrow Dependencies)和宽依赖(Wide Dependencies)。
窄依赖是指每个父RDD都之多被一个RDD的分区使用，而宽依赖是多个子RDD的分区依赖一个父RDD的分区。例如map，filter操作是窄依赖，而join，groupbykey是宽依赖。

Q2: 任务的调度？如何做容错（失败的任务和执行慢的任务）？

A2: 计算与数据就近原则。在作业中如果某个任务执行缓慢，系统会在其他节点上执行该任务的副本，与MapReduce推测执行做法类似，取最先得到的结果作为最终的结果。

Q3: 什么是DAG ? 

Q4: Job/Stage/Task的并行执行关系？

一个Action生成一个Job，一次shuffle划分2个stage，task根据RDD Partition 一一对应生成。

Q5: Spark vs MapReduce

A5: 内存迭代计算，任务依赖关系用DAG表示，支持map，reduce以外更丰富的算子。

Q6: Spark 如何做内存管理？

Q7: Spark SQL 长短作业的公平调度？

Q8: Shuffle 原理和优化？

Q9: Spark Join 优化?

A9: https://www.slideshare.net/databricks/optimizing-apache-spark-sql-joins

Q10: 如何存储和调度非常大（内存不够）的RDD？

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

Q3: Hdfs 上传下载文件的交互流程？

Q4: Yarn如何做HA?

> 分布式一致性：Zookeeper，分布式锁和主从选举
