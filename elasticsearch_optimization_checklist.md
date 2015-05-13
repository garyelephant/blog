# Elasticsearch Optimization Checklist

## TODO
*	application level:是否要在query请求所占的资源上做一些限制
*	application level:是否考虑配置routing

## 假设
*	hardware 假设
*	index/query rate假设
*	elasticsearch用户运行elasticsearch

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
$ cp /etc/security/limits.conf /etc/security/limits.conf.bak

$ cat /etc/security/limits.conf | grep -v "elasticsearch" > /tmp/system_limits.conf

$ echo "root      hard    nofile      50000" >> /tmp/system_limits.conf

$ echo "root      soft    nofile      50000" >> /tmp/system_limits.conf

$ mv /tmp/system_limits.conf /etc/security/limits.conf
```

*    configure the maximum map count

 set it permanently by modifying vm.max_map_count setting in your /etc/sysctl.conf.[2][2]
 
```
# virtual Memory
$ cp /etc/sysctl.conf /etc/sysctl.conf.bak

$ cat /etc/sysctl.conf | grep -v "vm.max_map_count" > /tmp/system_sysctl.conf

$ echo "vm.max_map_count=262144" >> /tmp/system_sysctl.conf

$ mv /tmp/system_sysctl.conf /etc/sysctl.conf
```

或者临时修改？[\[7\]][7]
```
sysctl -w vm.max_map_count=262144
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

ES includes several recovery properties which improve both ElasticSearch cluster recovery and restart times. We have shown some sample values below. The value that will work best for you depends on the hardware you have in use, and the best advice we can give is to test, test, and test again.

```
cluster.routing.allocation.node_concurrent_recoveries:4
```
This property is how many shards per node are allowed for recovery at any moment in time. Recovering shards is a very IO-intensive operation, so you should set this value with real caution.

```
cluster.routing.allocation.node_initial_primaries_recoveries:18
```
This controls the number of primary shards initialized concurrently on a single node. The number of parallel stream of data transfer from node to recover shard from peer node is controlled by indices.recovery.concurrent_streams. The value below is setup for the Amazon instance, but if you have your own hardware you might be able to set this value much higher. The property max_bytes_per_sec (as its name suggests) determines how many bytes to transfer per second. This value again need to be configured according to your hardware.
```
indices.recovery.concurrent_streams: 4
indices.recovery.max_bytes_per_sec: 40mb
```

All of the properties described above get used only when the cluster is restarted.[\[5\]][5]

*	Threadpool Properties Prevent Data Loss[\[5\]][5]
ElasticSearch node has several thread pools in order to improve how threads are managed within a node. At Loggly, we use bulk request extensively, and we have found that  setting the right value for bulk thread pool using threadpool.bulk.queue_size property is crucial in order to avoid data loss or _bulk retries
```
threadpool.bulk.queue_size: 3000
```

This property value is for the bulk request. This tells ES the number of  requests that can be queued for execution in the node when there is no thread available to execute a bulk request. This value should be set according to your bulk request load. If your bulk request number goes higher than queue size, you will get a RemoteTransportException as shown below.

Note that in ES the bulk requests queue contains one item per shard, so this number needs to be higher than the number of concurrent bulk requests you want to send if those request contain data for many shards. For example, a single bulk request may contain data for 10 shards, so even if you only send one bulk request, you must have a queue size of at least 10. Setting this value “too high” will chew up heap in your JVM, but does let you hand off queuing to ES, which simplifies your clients.

You either need to keep the property value higher than your accepted load or gracefully handle RemoteTransportException in your client code. If you don’t handle the exception, you will  end up losing data. We simulated the exception shown below by sending more than 10 bulk requests with a queue size of 10.
```
RemoteTransportException[[<Bantam>][inet[/192.168.76.1:9300]][bulk/shard]]; nested: EsRejectedExecutionException[rejected execution (queue capacity 10) on org.elasticsearch.action.support.replication.TransportShardReplicationOperationAction$AsyncShardOperationAction$1@13fe9be];
```


*	Watch Out for delete_all_indices! [\[5\]][5]
It’s really important to know that the curl API in ES does not have very good authentication built into it. A simple curl API can cause all the indices to delete themselves and lose all data. This is just one example of a command that could cause a mistaken deletion:
```
curl -XDELETE ‘http://localhost:9200/*/’
```
To avoid this type of grief, you can set the following property:
```
action.disable_delete_all_indices: true
```
This will make sure when above command is given, it will not delete the index and will instead result in an error.


*    cluster settings 优化
PUT _cluster/settings
```
put /_cluster/settings
{
     "persistent" : {
         "indices.store.throttle.max_bytes_per_sec":"20mb",
         "indices.breaker.fielddata.limit":"60%",
         "indices.breaker.request.limit":"40%",
         "indices.breaker.total.limit":"70%"
     }
}
```
上面的都是默认值。如果日志中常出现`index throttled`~~并且磁盘IO不高~~ `"indices.store.throttle.max_bytes_per_sec"`可以更大；如果日志中经常出现`java.lang.OutOfMemoryError`, 可以减小"indices.breaker.fielddata.limit"`,`"indices.breaker.request.limit"`,`"indices.breaker.total.limit"`的值。

>**TIP**: In [Fielddata Size](http://www.elastic.co/guide/en/elasticsearch/guide/master/_limiting_memory_usage.html#fielddata-size), we spoke about adding a limit to the size of fielddata, to ensure that old unused fielddata can be evicted. The relationship between indices.fielddata.cache.size and indices.breaker.fielddata.limit is an important one. If the circuit-breaker limit is lower than the cache size, no data will ever be evicted. In order for it to work properly, the circuit breaker limit must be higher than the cache size.

*	disk based allocation strategy[\[6\]][6]
```
PUT /_cluster/settings -d '{
    "transient" : {
        "cluster.routing.allocation.disk.threshold_enabled" : true,
        "cluster.routing.allocation.disk.watermark.low" : "85%",
        "cluster.routing.allocation.disk.watermark.high" : "90%"
    }
}'
```

`cluster.routing.allocation.disk.watermark.low` controls the low watermark for disk usage. It defaults to 85%, meaning ES will not allocate new shards to nodes once they have more than 85% disk used. It can also be set to an absolute byte value (like 500mb) to prevent ES from allocating shards if less than the configured amount of space is available.

`cluster.routing.allocation.disk.watermark.high` controls the high watermark. It defaults to 90%, meaning ES will attempt to relocate shards to another node if the node disk usage rises above 90%. It can also be set to an absolute byte value (similar to the low watermark) to relocate shards once less than the configured amount of space is available on the node.




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

[5]: https://www.loggly.com/blog/nine-tips-configuring-elasticsearch-for-high-performance/ "9 Tips on ElasticSearch Configuration for High Performance"

[6]: http://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-allocation.html#disk "Disk-based Shard Allocation"

[7]: http://stackoverflow.com/questions/11683850/how-much-memory-could-vm-use-in-linux "how much memory could vm use in linux"

---

> Written with [StackEdit](https://stackedit.io/).