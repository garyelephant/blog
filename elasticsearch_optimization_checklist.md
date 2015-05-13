# Elasticsearch Optimization Checklist

## hardware Level
这个暂时不考虑了


## System Level
*    switch off swap [1][1]

```
$ sudo swapoff -a
```

*    Max Open File Descriptors 设置为32k~64k
```
# max open file descriptors
echo "root      hard    nofile      50000" >> /etc/security/limits.conf
echo "root      soft    nofile      50000" >> /etc/security/limits.conf
```

*    configure the maximum map count

 set it permanently by modifying vm.max_map_count setting in your /etc/sysctl.conf.[2][2]
 
 ```
 # virtual Memory
echo "vm.max_map_count=262144" >> /etc/sysctl.conf
 ```


## Application Level
*    ES_HEAP_SIZE=Xg
Ensure that the min (Xms) and max (Xmx) sizes are the same to prevent the heap from resizing at runtime, a very costly process.

*    Give Half Your Memory to Lucene

*    Don’t Cross 32 GB!

*   enable mlockall (elasticsearch.yml)

```
bootstrap.mlockall: true
```

* discovery (elasticsearch.yml)

```
discovery.zen.ping.multicast.enabled: false
discovery.zen.ping.unicast.hosts: master_node_list
```

*    recovery strategy (elasticsearch.yml)

```
# if you have 10 nodes
gateway.recover_after_nodes: 8
gateway.expected_nodes: 10
gateway.recover_after_time: 10m
```

* merge rate (_cluster/settings)
```
put _cluster/settings
{
     "persistent" : {
         "indices.store.throttle.max_bytes_per_sec":"20mb" # this is default
     }
}
```

*	index template 优化

利用好不同template之间的order关系
默认所有field都是not_analyzed
默认numeric, date, string(not_analyzed), geo_point类型的field都使用[doc_values][4] 形式的fielddata
Doc values can be enabled for numeric, date, Boolean, binary, and geo-point fields, and for not_analyzed string fields. They do not currently work with analyzed string fields. Doc values are enabled per field in the field mapping, which means that you can combine in-memory fielddata with doc values.

*    安装监控工具

```
elastic marvel
```

---
## 验证方法
GET /_nodes/process可以看到

```
"max_file_descriptors": 64000, 
"mlockall": true 
```

---
## Appendix A Base Template

```
PUT _template/base
{
  "order": 0,
  "template": "*",
  "settings": {
    "index.refresh_interval": "120s",
    "index.number_of_replicas": "1",
    "index.number_of_shards": "10",
    "index.routing.allocation.total_shards_per_node": "2",
    "index.search.slowlog.threshold.query.warn": "10s",
	"index.search.slowlog.threshold.query.info": "5s",
	"index.search.slowlog.threshold.fetch.warn": "1s",
	"index.search.slowlog.threshold.fetch.info": "800ms",
	"index.indexing.slowlog.threshold.index.warn": "10s",
	"index.indexing.slowlog.threshold.index.info": "5s"
  },
  "mappings": {
    "_default_": {
      "dynamic_templates": [
        {
          "integer field": {
            "mapping": {
              "doc_values": true,
              "type": "integer"
            },
            "match": "*",
            "match_mapping_type": "integer"
          }
        },
        {
          "date field": {
            "mapping": {
              "doc_values": true,
              "type": "date"
            },
            "match": "*",
            "match_mapping_type": "date"
          }
        },
        {
          "long field": {
            "mapping": {
              "doc_values": true,
              "type": "long"
            },
            "match": "*",
            "match_mapping_type": "long"
          }
        },
        {
          "float field": {
            "mapping": {
              "doc_values": true,
              "type": "float"
            },
            "match": "*",
            "match_mapping_type": "float"
          }
        },
        {
          "double field": {
            "mapping": {
              "doc_values": true,
              "type": "double"
            },
            "match": "*",
            "match_mapping_type": "double"
          }
        },
        {
          "byte field": {
            "mapping": {
              "doc_values": true,
              "type": "byte"
            },
            "match": "*",
            "match_mapping_type": "byte"
          }
        },
        {
          "short field": {
            "mapping": {
              "doc_values": true,
              "type": "short"
            },
            "match": "*",
            "match_mapping_type": "short"
          }
        },
        {
          "binary field": {
            "mapping": {
              "doc_values": true,
              "type": "binary"
            },
            "match": "*",
            "match_mapping_type": "binary"
          }
        },
        {
          "geo_point field": {
            "mapping": {
              "doc_values": true,
              "type": "geo_point"
            },
            "match": "*",
            "match_mapping_type": "geo_point"
          }
        },
        {
          "string fields": {
            "mapping": {
              "index": "not_analyzed",
              "omit_norms": true,
              "doc_values": true,
              "type": "string"
            },
            "match": "*",
            "match_mapping_type": "string"
          }
        }
      ],
      "_all": {
        "enabled": false
      }
    }
  }
}
```

---
[1]: http://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#_swapping_is_the_death_of_performance "swapping is the death of performance"

[2]: http://www.elastic.co/guide/en/elasticsearch/guide/current/_file_descriptors_and_mmap.html "file descriptors and mmap"

[3]: http://www.elastic.co/guide/en/elasticsearch/guide/current/_important_configuration_changes.html#_recovery_settings "recovery settings"

[4]: http://www.elastic.co/guide/en/elasticsearch/guide/current/doc-values.html#_enabling_doc_values "Enabling Doc Values"

---

> Written with [StackEdit](https://stackedit.io/).