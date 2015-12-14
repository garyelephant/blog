# A Journey in ELK

---
## TODO

kafka读写message：

*	partition均匀写
*	consumer僵死(logstash)
*	kafka监控

logstash

*	用logstash满足各种各样的用户日志归一化需求

Elasticsearch 非实时数据的聚合思路：

*	elasticsearch aggs, 存在的问题：多层aggs, 非实时的聚合，CPU瓶颈。
*	logstash, metric, aggregate  优点，局限性
*	elasticsearch_aggregator 优点，局限性
*	spark 优点，局限性

数据可视化上的思考：

*	更简单易用的UI
*	从配置界面上的可视化元素到模型的总结（运维，基础用户行为分析[渠道转化率，激活量，活跃用户，留存率]，高级用户分析[用户画像，个性化推荐]）

整个架构流程上的思考：

*	吞吐量，延时，丢失率



> Written with [StackEdit](https://stackedit.io/).