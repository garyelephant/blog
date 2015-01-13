# Elasticsearch 2014年12月简报

---

## Elasticsearch Updates
*	Elasticsearch 1.4.2发布了
	改进和bug fix，下载地址:[Elasticsearch 1.4.2 Download](http://www.elasticsearch.org/downloads/1-4-2)
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
改进和bug fix，下载地址:[Elasticsearch 1.3.7 Download](http://www.elasticsearch.org/downloads/1-3-7)

*   Elasticsearch, Logstash, Kibana, Marvel的官方documents, tutorial现在都统一放在了这里：http://www.elasticsearch.org/guide/。以后看docs统统到这里！
这里的logstash的documents比logstash.net的更详尽，以后logstash.net的documents也会逐渐停止更新。


## Elasticsearch Ecosystem Updates
*	 Logstash 1.5.0 Beta 1发布了
1.5.0主要的变化是：
	 *    plugin management：插件与Logstash主程序分离了，使用 rubygems.org来发布插件，另外附带一个plugin命令来管理插件。所以现在Logstash与Elasitcsearch的插件管理方式相似了。
	 *    performance improvements：grok filter的正则匹配做了优化，如官方测试了一下COMBINEDAPACHELOG，相比1.4.2,性能近乎提高了1倍。json的序列化与反序列化性能提升超过了1倍。
	 *     Apache Kafka integration：增加了对kafka input,output的支持.
	 *     improved security：We have improved the security of the Elasticsearch output, input, and filter by adding authentication and transport encryption support.
	 *     bug fixes and enhancements:
		*    Allow storing ‘metadata’ to an event which is not sent/encoded on output. This eliminates the need for intermediate fields for example, while using date filter.([#1834](https://github.com/elasticsearch/logstash/issues/1834), [#LOGSTASH-1798](https://logstash.jira.com/browse/LOGSTASH-1798))
		*     Filters that generated events (multiline, clone, split, metrics) now propagate those events correctly to future conditionals ([#1431](https://github.com/elasticsearch/logstash/issues/1431))
		*     Elasticsearch output: Logstash will not create a `message.raw `field by default now. Message field is `not_analyzed` by Elasticsearch and adding a multi-field was essentially doubling the disk space required, with no benefit

 ```
 安装kafka input插件：
 $LS_HOME/bin/plugin install logstash-input-kafka
 安装kafka output插件：
 $LS_HOME/bin/plugin install logstash-output-kafka
 ```

*	 Kibana 4 Beta3 发布了
	*    interactive charts and dashboards
	*     scripted fields
	*     highlighting and a new format for _source
	*     hit links
	*     metric visualization


链接见[ Kibana 4 Beta3 ](http://www.elasticsearch.org/blog/kibana-4-beta-3-now-more-filtery/)

*	NEST 1.3.0 发布了elasticsearch 的.net client, see [release note](https://github.com/elasticsearch/elasticsearch-net/releases/tag/1.3.0)

*	Marvel 1.3.0 发布了，主要更新如下：
	*    sense中加入了1.4.x新增的api自动补全提示。
	*    增加了对HTTPS的支持。
	*    monitoring ui增加了对charts for new circuit breakers introduce with ES 1.4.0, a chart to plot circuit break limit,  a charts for Query Cache, charts for index throttling, charts to expose memory usage of the index writer and version map, 
	*     sense Added: a settings to allow disabling mappings and/or indices autocomplete. This is useful for extremely large deployments where parsing by the browser is unrealistic.
	*     sense added: Cluster Reroute API, Get Field Mappings API, Query Cache parameters to the Search API, Analyze API, Validate Query API,  Put Percolator API, cluster.routing.allocation.* settings, weight param to the Function Score query.,Flush API, show_term_doc_count_error parameter to the Terms Aggregation, Update API, _geo_distance as a sort option,  Updated the Significant Terms aggregation to 1.4.0 features, metadata fields to the Mapping API, Get Index API, Scripted Metric Aggregation, simple_query_string query, Updated the More Like This Query to 1.4.0 features, min_childeren, max_children options to the has_child query and filter, Updated execution hint options in terms and significant terms aggs, transform section of Mappings API, indexed scripts and templates, Geo Bounds aggregation, Top Hits aggregation, collect_mode option the Terms aggregation,  Percentiles Rank aggregation, Disk Threshold Allocator settings

完整的更新列表见[marvel 1.3.0 released](http://www.elasticsearch.org/blog/marvel-1-3-0-released/)


## Amazing Slides & tutorials & videos
*	exciting logstash plugin ecosystem changes
这篇blog讲了logstash 1.5.x的插件管理方式及开发方式。
http://www.elasticsearch.org/blog/plugin-ecosystem-changes/

*	Maintaining performance in distributed systems by Elasticsearch Inc
https://speakerdeck.com/elasticsearch/maintaining-performance-in-distributed-systems

*	setting up and using Kibana 4 Beta
http://amsterdam.luminis.eu/2014/12/01/experiment-with-the-kibana-4-beta/#more-76

*	[Video]Short and sweet: Demo of Weave to tie together Elasticsearch, Docker, and Apache Spark
https://www.youtube.com/watch?v=BSY9rnK9QBs&list=UUmIz9ew1lA3-XDy5FqY-mrA

*	At last week’s Elasticsearch meetup in Chicago, Dan Crumb (of our lovely meetup host, Vodori) gave a demonstration using Docker and Fig to easily run Elasticsearch in containers on a laptop. He’s now [shared the code and the how-to](https://github.com/vodori/es-fig-docker/) behind his demonstration, and [video](http://vimeo.com/113497975) is available from the meetup, as well.

*	Gert Leenders shared some in-depth tips on the [optimization of relevance scores in Elasticsearch](https://www.voxxed.com/blog/2014/12/advanced-scoring-elasticsearch/), including how boosting works, as well as boosting by date and by popularity.

*	Vadiraj Joish has a tutorial explaining the fundamentals of Logstash, as well as how to install and configure [Logstash on Linux with Elasticsearch, Redis, and Nginx](http://www.thegeekstuff.com/2014/12/logstash-setup).ELK入门。

*	ClusterHQ’s new project, Eliot, is a logging system for complex distributed systems. See [how Eliot uses the ELK stack](https://clusterhq.com/blog/eliot-0-6-logging-distributed-systems-python/) to deep-dive into their logs.

*	Hayssam Saleh explains performance [tuning for Elasticsearch](http://blog.ebiznext.com/2014/12/16/elasticsearch-performance-tuning/)

*	Elasticsearch官方视频网站 http://vimeo.com/elasticsearch

*	[video Elasticsearch官方视频网站]Colin Goodheart-Smithe on DIY Aggregations for Elasticsearch


## Meetups in China
*	Nothing

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