# A Journey in ELK

---
## TODO

自动化工具salt

kafka读写message：

*	partition均匀写
*	consumer僵死(logstash)
*	kafka监控

任务调度系统（celery）

logstash

*	用logstash满足各种各样的用户日志归一化需求


Elasticsearch

*	数据重复写入导致计算结果不正确的问题
数据为什么会重复写入

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

*	spark 优点，局限性


业务数据监控：

*	elastalert

*	使用机器学习更准确的监控数据趋势变化

Docker化：

*	目的
链接我之前写的博客。

*	成果，思考：
未来的数据中心，我们需要DCOS.

数据可视化上的思考：

*	更简单易用的UI
思路：kibana 4作为数据可视化基础组件，负责展示图表，kibana 4之上再套一层自己开发的UI，目的是简化数据可视化的配置，主要负责用户点击后生成kibana图表。

*	从配置界面上的可视化元素到模型的总结（运维，基础用户行为分析[渠道转化率，激活量，活跃用户，留存率]，高级用户分析[用户画像，个性化推荐]）

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