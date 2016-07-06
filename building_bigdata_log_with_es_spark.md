

## 用户界面（Web前端篇）

## 全文索引篇

### 分词

### 用es实现google，百度搜索的Query：

功能：支持全文查找(优先精确匹配、同时包括部分匹配结果)，高亮，事件聚合

```
{
  "query": {
    "bool": {
      "filter": {
        "range": {
          "@timestamp": {
            "format": "yyyy-MM-dd HH:mm:ss",
            "from": "2016-07-06 11:21:09",
            "include_lower": true,
            "include_upper": true,
            "time_zone": "+08:00",
            "to": "2016-07-06 11:51:09"
          }
        }
      },
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
  }
}
```

## 即时计算篇

Why Not Elasticsearch Aggregations API ?

Using Spark SQL

Problem with Elasticsearch Scroll API:

