# Presto 关键技术点

## 架构

![architecture](./presto_images/architecture.png)

## MPP vs MapReduce

![presto vs mapreduce](./presto_images/presto-vs-mapreduce.png)

---

## FAQ

1. "Query", "Stage","Task","Split","Driver","Pipeline", "Operator" ?

A query is a single execution of SQL. 

A query has stages. A stage executes a query plan fragment. 

A stage has tasks. All tasks in the stage execute the same plan fragment.  Generally there is at most one Task per stage per worker node, but the system can be configured to allow multiple. 

A task has pipelines. A pipeline is basically a template for drivers.  When the plan fragment in a stage is broken down into operators, we may end up with multiple pipelines.  For example, a join ends up with a pipeline for the "probe" and a pipeline for the “build". 

A pipeline has drivers.  A driver is an instance of the template in a pipeline.  Typically there is one of these per split.  Some pipelines are not created based on splits and only have a single driver instance. 

A driver has operators.  The driver contains a list of operators.  The driver “drives” pages of data through the operator chain. 

Operators do the actual data processing in Presto.  Example operators are: table scan, filter, project, aggregate, join, etc. An operator optionally consumes pages and optionally produces output pages. 

A split is a part of a table. 

2. 为什么Presto快？


---

## References

https://www.slideshare.net/GuorongLIANG/facebook-presto-presentation

http://prestodb.rocks/internals/the-fundamentals-data-distribution/

盘点SQL on Hadoop中用到的主要技术: http://sunyi514.github.io/2014/11/15/%E7%9B%98%E7%82%B9sql-on-hadoop%E4%B8%AD%E7%94%A8%E5%88%B0%E7%9A%84%E4%B8%BB%E8%A6%81%E6%8A%80%E6%9C%AF/

---

## TODO

https://tech.meituan.com/presto.html

https://www.slideshare.net/AGrishchenko/mpp-vs-hadoop

https://0x0fff.com/hadoop-vs-mpp/

https://www.linkedin.com/pulse/hadoop-vs-mpp-anoop-kumar-goyal

https://venturebeat.com/2013/03/19/how-to-conquer-big-data-with-mapreduce-mpp/

http://www.vldbsolutions.com/blog/mapreduce-mpp/

https://www.flydata.com/blog/introduction-to-massively-parallel-processing/

http://datascientists.info/blog/2013/04/26/hadoop-mpp/

http://www.zdnet.com/article/mapreduce-and-mpp-two-sides-of-the-big-data-coin/
