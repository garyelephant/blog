
# Building Realtime Log search and analysis system with Elasticsearch and Spark

## 用户界面（Web前端篇）

## 全文索引篇

### 分词

### 用es实现google，百度搜索的Query：

功能：支持全文查找(优先精确匹配、同时包括部分匹配结果)，高亮，事件聚合，排序（先根据score排序，再根据时间排序）

```
{
    "query": {
        "bool": {
            "filter": [
                {
                    "range": {
                        "@timestamp": {
                            "format": "yyyy-MM-dd HH:mm:ss", 
                            "from": "2016-07-06 11:21:49", 
                            "include_lower": true, 
                            "include_upper": true, 
                            "time_zone": "+08:00", 
                            "to": "2016-07-06 11:51:49"
                        }
                    }
                }
            ], 
            "minimum_should_match": "1", 
            "should": [
                {
                    "match": {
                        "raw_message": {
                            "boost": 2, 
                            "query": "lecloud.com", 
                            "type": "phrase"
                        }
                    }
                }, 
                {
                    "query_string": {
                        "default_field": "raw_message", 
                        "query": "lecloud.com"
                    }
                }
            ]
        }
    }, 
    "size": 1000,
    "sort": [
        {
            "_score": {}
        }, 
        {
            "@timestamp": {
                "order": "desc"
            }
        }
    ],
        "highlight": {
        "fields": {
            "*": {}
        }, 
        "number_of_fragments": 0, 
        "post_tags": [
            "</mark>"
        ], 
        "pre_tags": [
            "<mark style='background:#ffff00;'>"
        ]
    }
}
```

## 即时计算篇

Why Not Elasticsearch Aggregations API ?

Using Spark SQL

Problem with Elasticsearch Scroll API:

