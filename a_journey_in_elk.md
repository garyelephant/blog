# A Journey in ELK

---

> 这几年用ELK构建实时日志分析服务过程中的所思所想和所作所为。

---

## TODO

万恶的用户日志格式：

*	以前我们每收到一个分析需求，接入一种用户日志，至少需要几天时间。我们曾经考虑过实现一个日志格式定义神器，使用起来极其简单，能适配用户app输出的千奇百怪的日志，大量减少与用户沟通日志格式的时间并增加沟通中的确定性——最终我们陷入万劫不复。

*	最快接入日志格式的方案：
	*	向用户推广日志格式设计规范，简化日志解析成本（人力，服务器资源的消耗）
	*	实现自动化接入日志的系统

现在我们只需要几分钟即可接入用户日志。

自动化工具salt

kafka读写message：

*	partition均匀写
*	consumer僵死(logstash)，自动重启对应logstash instance。
*	kafka监控

任务调度系统（celery）

logstash

*	用logstash满足各种各样的用户日志归一化需求

*	logstash with cgroups

Elasticsearch

*	数据重复写入导致计算结果不正确的问题
数据为什么会重复写入

*	如何用aggregations: aggs非常灵活，几乎能满足所有聚合需求，但是它不适合对大量docs做聚合。
迄今为止，elasticsearch 的aggregations是我最喜欢的数据操作的API，kibana是我最喜欢的数据可视化方案，它们两个的组合也释放了无穷的魅力，但是aggregations确实不适合对大量docs做聚合。

我们的集群对num_doc:12亿，primary总共1.5T, mappings中有100+ fields的3个index做aggs时，整个集群的负载非常高, 其他的query执行延时也很长，indexing 也受到严重影响。例如做基于时间的数据聚合，如果涉及的docs非常多，可以缩短时间段，如从最近几天缩短到最近几小时，甚至几分钟，这样aggs执行非常快，消耗的CPU也很少。对于大量的离线聚合需求，如出一个星期的报表，如果数据量巨大，还是请出hadoop, spark这些吧。如果需要数据可视化，可以把离线job的结果再写回es，用kibana做可视化。

同时我们在elasticsearch官网看到这么一张图，它聚合了最近2天的数据却非常快，原因是数据量只有2千多条。

![Figure 39. Kibana—a real time analytics dashboard built with aggregations](https://www.elastic.co/guide/en/elasticsearch/guide/current/images/elas_29in03.png)

图片来源：https://www.elastic.co/guide/en/elasticsearch/guide/current/_the_sky_8217_s_the_limit.html

*	目前有3个方案，防止集群因aggs不可用：
（1）es集群中增加client node, client node 前面放置nginx，由nginx负责自动禁掉可能导致集群不可用的aggs request。这些request的特征是aggs的嵌套层数较多且包含percentile_ranks等aggs，涉及的docs数较多。
工作中涉及 A. 上线elasticsearch client node, B. nginx学习和上线, C. 用Lua以nginx module的形式开发一个禁掉aggs request的业务逻辑
（2）人为禁止耗资源的aggs的使用，但不好限制。
（3）挖掘数据较多的index的用户需求，使用elasticsearch数据聚合工具预先聚合数据，就像现在的监控屏幕上的数据一样。


*	search slowlog, indexing slowlog
两个es cluster,一个业务cluster, 一个监控cluster写slowlog

*	search优化
search原理后续整理

*	使用script做计算

*	curator好工具

Elasticsearch 非实时数据的聚合思路：

*	非实时的需求-报表需求

*	aggs资源消耗
不同的aggs计算延迟可能相差很大， aggs的资源消耗与延时与下面的因素有关：aggs涉及doc的数量，实时聚合一般聚合的是最近几秒到几分内的数据，doc数量一般较少；而对于非实时的报表类的聚合需求，一般聚合1天甚至7天以上的数据，如果涉及doc数量较大（对于我们来说是几百亿，与软硬件配置相关，如果aggs中有percential_ranks等更耗CPU的aggs,计算几十亿的doc就很慢），aggs的嵌套层数，是否使用消耗资源的aggs.见`Appendix A`中一个延时很短的aggs。

* 多个用户同时做非实时的aggs时，elasticsearch服务几乎不可用。

*	elasticsearch aggs, 优点(适合经常变化，不固定的聚合需求，用query+aggs很容易满足)，存在的问题：多层aggs, 非实时的聚合，CPU瓶颈。

*	logstash, 通过mutate做字段连接, logstash-filter-metric做event count  优点，局限性(只能满足很少的需求)

*	elasticsearch_aggregator 优点，局限性

这个project为海量数据的非实时聚合提供了一种可能性，功能虽然有限，但能一定程度上免去了hadoop, spark生态系统的学习成本。我们开源出来就是希望和你一起打磨这款产品，褒扬协助也好，辱骂唾弃也罢，我们请你给个态度。

*	spark 优点，局限性


*	ELK on Mesos


业务数据监控：

*	elastalert

*	使用机器学习更准确的监控数据趋势变化
https://plot.ly/python/polynomial-fits/


Docker化：

*	目的
链接我之前写的博客。

*	成果，思考：
未来的数据中心，我们需要DCOS.

数据可视化上的思考：

*	更简单易用的UI
思路：kibana 4作为数据可视化基础组件，负责展示图表，kibana 4之上再套一层自己开发的UI，目的是简化数据可视化的配置，主要负责用户点击后生成kibana图表。

*	从配置界面上的可视化元素到模型的总结（运维，基础用户行为分析[渠道转化率，激活量，活跃用户，留存率]，高级用户分析[用户画像，个性化推荐]）

对业务的理解：

*	基于事件的实时在线人数统计的实现方式。

整个架构流程上的思考：

*	吞吐量，延时，丢失率，跨机房

---

### 思考-分享什么？

*	分享我们的技术栈

*	分享我们踩过的坑

*	分享我们开源的软件

### 我的观点

*	未来的机器学习必定是简单易用的，人人都有权利使用机器学习

*	Dcos是未来的data center，

*	容器化是未来云计算的趋势，分享我之前的博文。

---

### References

1.	我的trello里面的elk优化记录

2.	Understanding the Trade-offs of percentiles aggs
https://www.elastic.co/guide/en/elasticsearch/guide/current/percentiles.html#_understanding_the_trade_offs_2


## Appendix A 一个延时较短的aggs示例
每天index大小:40million左右docs, 单份数据: 20GB, aggs平均延时:1.03s
```
# query
{
  "query": {
    "filtered": {
      "query": {
        "query_string": {
          "query": "*",
          "analyze_wildcard": true
        }
      },
      "filter": {
        "bool": {
          "must": [
            {
              "query": {
                "query_string": {
                  "analyze_wildcard": true,
                  "query": "*"
                }
              }
            },
            {
              "range": {
                "@timestamp": {
                  "gte": 1450076010347,
                  "lte": 1450162410347
                }
              }
            }
          ],
          "must_not": []
        }
      }
    }
  },
  "size": 0,
  "aggs": {
    "2": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "10m",
        "pre_zone": "+08:00",
        "pre_zone_adjust_large_interval": true,
        "min_doc_count": 1,
        "extended_bounds": {
          "min": 1450076010341,
          "max": 1450162410341
        }
      },
      "aggs": {
        "3": {
          "filters": {
            "filters": {
              "domain:ww*": {
                "query": {
                  "query_string": {
                    "query": "domain:ww*",
                    "analyze_wildcard": true
                  }
                }
              },
              "domain:us*": {
                "query": {
                  "query_string": {
                    "query": "domain:us*",
                    "analyze_wildcard": true
                  }
                }
              }
            }
          },
          "aggs": {
            "1": {
              "sum": {
                "field": "hits"
              }
            }
          }
        }
      }
    }
  }
}
```


> Written with [StackEdit](https://stackedit.io/).