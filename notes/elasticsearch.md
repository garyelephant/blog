# Elasticsearch 关键技术点汇总

## 关键技术点

### 写入(索引)数据的详细流程

* 路由策略

```
shard_id = hash(routing_id) % num_of_shards
```

* refresh / flush / translog 机制, 异步sync / 生成segment

* segment merge

参考：https://blog.csdn.net/jiaojiao521765146514/article/details/83753215

### 查询(搜索)的详细流程

* 路由策略

* 普通查询原理

![searching](./elasticsearch_images/search.jpeg)

参考：http://ginobefunny.com/post/elasticsearch_interview_questions/

* 聚合查询原理

### 集群管理

* 角色划分：master node / data node / coord node

* master 选主 / cluster state

* 跨集群查询

* 多租户

### Lucene 原理

* 倒排索引，相关性搜索：TF/IDF 原理

* 文件结构

* doc values / 文件系统缓存

### ES 调优经验

常见的调优策略：

https://mp.weixin.qq.com/s/Fvf9JcOc5oSRlLdHB4tYxA

---

## FAQ

1. Elasticsearch是如何实现Master选举的？

TODO: 用Paxos了吗？备选节点`node.master=true`为什么可以有偶数个？

2. 节点之间如何实现互相发现？

3. Master节点如何Failover, 如何防止brain split ?

4. Elasticsearch如何实现Document Update/Delete ?

```
删除和更新也都是写操作，但是Elasticsearch中的文档是不可变的，因此不能被删除或者改动以展示其变更；

delete，update是通过Lucene的.del文件实现的。

[delete]磁盘上的每个段都有一个相应的.del文件。当删除请求发送后，文档并没有真的被删除，而是在.del文件中被标记为删除。
该文档依然能匹配查询，但是会在结果中被过滤掉。当段合并时，在.del文件中被标记为删除的文档将不会被写入新段。

[update]在新的文档被创建时，Elasticsearch会为该文档指定一个版本号，当执行更新时，旧版本的文档在.del文件中被标记为删除，新版本的文档被索引到一个新段。
旧版本的文档依然能匹配查询，但是会在结果中被过滤掉。
```

5. 索引数据的详细流程 ?

6. 搜索的详细流程 ?

7. 性能调优？

8. 如何做聚合？聚合的结果是100%准确吗？

9. Lucene原理是什么？

10. 分布式相关问题：es的节点有哪些角色，都是什么功能；节点之间如何通信；如何做节点发现？

master, data, searcher, coord(client请求到的节点，动态不固定)

11. 分布式相关问题：分片创建策略，副本复制策略, 读写数据时的分片路由策略，副本容错策略，如何做到读写的计算请求尽可能负载均衡 ?

12. doc value原理及用法？
 
13. Index merge 原理？

14. Index recovery 原理？

15. 如何从ES获取大量数据？ES内部是如何实现的？

Scroll API的实现。

---

## References

http://ginobefunny.com/post/elasticsearch_interview_questions/

Lucene的索引文件格式(1): http://www.cnblogs.com/forfuture1978/archive/2009/12/14/1623597.html

Lucene的索引文件格式(2): http://www.cnblogs.com/forfuture1978/archive/2009/12/14/1623599.html

ES内存那点事 https://elasticsearch.cn/article/32
