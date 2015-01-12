# Elasticsearch 2014年12月简报

---

## Elasticsearch Updates
*	Elasticsearch 1.4.2发布了
	一些改进和bug fix，下载地址:[Elasticsearch 1.4.2 Download](http://www.elasticsearch.org/downloads/1-4-2)
	*    bug fix:
		*    If a node holding a primary shard was restarted while a replica shard was still recovering from the primary, it could delete the transaction log on the primary, resulting in data loss.
		*    he ScriptService can deadlock entire nodes if the script index is recovering.
		*    Forcefully releasing the Index Writer lock can cause shard corruption. 
	*    enhancement 
		*   The disk allocation decider, which makes decisions about shard allocation based on free disk space, is now significantly faster and improves recovery speed after a cluster restart.
		*    Snapshots made to a shared file system are much faster than before. 
		*     Unnecessary cluster state updates have been reduced, which reduces network traffic and speeds up recovery.
		*     The index stats API shouldn’t be blocked by shard recovery.

*	Elasticsearch 1.3.7发布了
一些改进和bug fix，下载地址:[Elasticsearch 1.3.7 Download](http://www.elasticsearch.org/downloads/1-3-7)
*   Elasticsearch, Logstash, Kibana, Marvel的官方documents, tutorial现在都统一放在了这里：http://www.elasticsearch.org/guide/。以后看docs统统到这里！
这里的logstash的documents比logstash.net的更详尽，以后logstash.net的documents也会逐渐停止更新。

## Elasticsearch Ecosystem Updates


## Amazing Slides & tutorials & videos


## Meetups in China


##References
1.	Elasticsearch 1.4.2 and 1.3.7 releasedDecember 16, 2014 http://www.elasticsearch.org/blog/elasticsearch-1-4-2-released/
2.	This Week in ElasticsearchDecember 3, 2014 http://www.elasticsearch.org/blog/2014-12-03-this-week-in-elasticsearch/
3.	This week in ElasticsearchDecember 10, 2014 http://www.elasticsearch.org/blog/2014-12-10-this-week-in-elasticsearch/
4.	This Week in ElasticsearchDecember 17, 2014 http://www.elasticsearch.org/blog/2014-12-17-this-week-in-elasticsearch/
5.	Kibana 4 Beta 3: Now more filteryDecember 16, 2014 http://www.elasticsearch.org/blog/kibana-4-beta-3-now-more-filtery/
6.	Logstash 1.5.0.Beta1 releasedDecember 11, 2014 http://www.elasticsearch.org/blog/logstash-1-5-0-beta1-released/
7.	Exciting Logstash Plugin Ecosystem ChangesDecember 12, 2014 http://www.elasticsearch.org/blog/plugin-ecosystem-changes/ 
8.	NEST and Elasticsearch.NET 1.3December 9, 2014 http://www.elasticsearch.org/blog/nest-and-elasticsearch-net-1-3/
9.	Marvel 1.3.0 releasedDecember 17, 2014 http://www.elasticsearch.org/blog/marvel-1-3-0-released/

> Written with [StackEdit](https://stackedit.io/).