## 大数据技术栈

大数据技术栈：Zookeeper, Hdfs, Yarn, Spark, HBase, Hive, Presto, Elasticsearch, Kafka, Redis, Flume, Logstash，mapd,neo4j，mysql，mongodb，文件格式（Parquet, Carbondata, Lucene, Arrow）

大数据与分布式系统重要理论：CAP, MapReduce, MPP, Paxos, 2PC, 3PC，MVCC

架构知识：数据仓库，流式计算，多维查询，搜索，日志收集，OLAP，OLTP，分布式锁和主从选举

设计模式：

数据结构与算法：排序、树、图基础算法，红黑树，BTree, HashMap, LinkedHashMap, skipList, 大数据算法

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

树的数据结构与常用算法（重点红黑树、BTree）

图的数据结构与常用算法

HashMap, LinkedHashMap, skipList

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

> 计算：Spark, Presto

Q1: Spark Join 优化?

A1: https://www.slideshare.net/databricks/optimizing-apache-spark-sql-joins

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
