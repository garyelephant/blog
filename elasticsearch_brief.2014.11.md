# Elasticsearch 2014年11月简报

---


## Elasticsearch Updates
*	Elasticsearch 1.4.0发布了，1.4.x中最新最稳定的版本。
这个版本主要加强了Es的稳定性和可靠性，内存管理更合理，加入数据校验以发现损坏的数据，主要变化如下：
	*    磁盘利用率默认每60s检查一次，磁盘满的日志由`DEBUG`改为`WARN`级别，对由磁盘满触发的shard在node之间的移动做了优化。
	*    Doc values把执行sort,aggregations时需要的fielddata写到了磁盘上，解决了默认用 in memory fielddata执行big query超出内存限制或占用过多内存的问题。近期发布的版本对doc values做了巨大的性能改进，根据官方的性能测试，它仅比fielddata慢了约10~25%，并且对于大部分的Queries, sorts, aggregations,scripts几乎感觉不到。
	*    通过Request circuit breaker加入了对单个请求的内存使用限制
	*    大量使用数据校验以检测数据损坏.
	*    Groovy替代MVEL成为默认的脚本语言。
	*    跨域访问（CORS）默认被禁止。
	*    Shard级别的Query cache使常用的aggregation, suggestions可以立即得到结果。Query cache目前只能用于search_type=count, 没有通过`now`指定时间的query中。
	*    新加入了3个aggregation类型：[filters (docs)](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-aggregations-bucket-filters-aggregation.html), [children (docs)](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-aggregations-bucket-children-aggregation.html) 以及 [scripted_metric (docs)](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-aggregations-metrics-scripted-metric-aggregation.html).
	*    一次获取index settings, mappings, warmers, aliases的新GET /index API。详见[doc]。(http://www.elasticsearch.org/guide/en/elasticsearch/reference/1.4/indices-get-index.html#indices-get-index)
>curl -XGET 'http://es_host:9200/your_index/_settings,_mappings, _warmers,_aliases'

	*    使用Flake IDs代替random UUID,提高了indexing效率和primary key查询效率，见这篇介绍[performance considerations for elasticsearch indexing](http://www.elasticsearch.org/blog/performance-considerations-elasticsearch-indexing/)


我们在[10月的Es简报中发布了Elasticsearch 1.4.0.Beta1](https://github.com/garyelephant/blog/blob/master/elasticsearch_brief.2014.10.md)中提到了更详细的变化。

*	Elasticsearch 1.3.6发布了，1.3.x中最新最稳定的版本，一堆bug fix，见[release notes](http://www.elasticsearch.org/downloads/1-3-6)。


## Elasticsearch Ecosystem Updates
*   Elasticsearch 安全工具Shield即将发布	
elasticsearch背后的公司elasticsearch.com即将在年底发布一款重量级产品：[Shield ](http://www.elasticsearch.org/overview/shield/)(elasticsearch的神盾特工局，专门保护elasticsearch的安全)。Shield预计是以elasticsearch插件的方式集成到其中。相信感受过此公司的[Marvel](http://www.elasticsearch.org/overview/marvel/)易用性的用户应该会很期待这款产品。Shield主要提供了4个功能：
	*    基于用户角色对Index读、写、查询的权限控制
	*    对基于LDAP和Active Directory验证的支持
	*    使用SSL/TLS对es node之间，client和node之间的传输加密
	*     记录安全相关的日志
详情见：[shield: you know, for security](http://www.elasticsearch.org/blog/shield-know-security-coming-soon/)

*	kibana 4 beta 2发布了
	*    现在支持地图了，利用aggregations在地图上地理位置相关的数据。
![Kibana4 beta 2 map support](https://github.com/garyelephant/blog/blob/master/images/elasticsearch_brief_2014.11_kibana_map_support.png)
	*    条形图可以以独立的方式按组绘制了，如在一个数据点上的html,css,php.这正是我们需要的功能。
![Kibana4 beta 2 group bar chart](https://github.com/garyelephant/blog/blob/master/images/elasticsearch_brief_2014.11_kibana_group_bar_chart.png)
	*     朴素的数据表，只展示数据
![Kibana4 beta 2 data table](https://github.com/garyelephant/blog/blob/master/images/elasticsearch_brief_2014.11_kibana_data_table.png)


## Amazing Slides & tutorials & videos
*	[migrating his Elasticsearch cluster from Canada to France with zero downtime](https://t37.net/migrate-your-es-cluster-from-one-continent-to-another-without-downtime.html)
*	[Having Fun: Python and Elasticsearch, Part 1](http://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1/)使用python入门Elasticsearch 
*	[The ELK Stack in a DevOps Environment](https://speakerdeck.com/elasticsearch/the-elk-stack-in-a-devops-environment)里面有一个在生产环境中Es,Logstash,Kibana配置的Best practices值得一看。
*	[Not all Nodes are Created Equal - Scaling Elasticsearch](https://speakerdeck.com/bleskes/not-all-nodes-are-created-equal-scaling-elasticsearch)扩展Elasticsearch。


## Meetups in China
*	Nothing


## Glossary 术语解释
*	fielddata fielddata的实现思路与倒排索引(inverted index)相反，Es使用倒排索引高效的完成search, 使用fielddata高效得完成aggregations,sorting,filter。fielddata的相关介绍[1](http://www.elasticsearch.org/guide/en/elasticsearch/guide/current/fielddata.html), [2](http://www.elasticsearch.org/guide/en/elasticsearch/guide/current/fielddata-intro.html)。

##References
1. shield: you know, for security http://www.elasticsearch.org/blog/shield-know-security-coming-soon/ 
2. Elasticsearch 1.4.0 and 1.3.5 released http://www.elasticsearch.org/blog/elasticsearch-1-4-0-released/
3. This week in ElasticsearchNovember 5, 2014 http://www.elasticsearch.org/blog/2014-11-05-this-week-in-elasticsearch/
4. This week in ElasticsearchNovember 12, 2014 http://www.elasticsearch.org/blog/2014-11-12-this-week-in-elasticsearch/
5. This Week in ElasticsearchNovember 19, 2014 http://www.elasticsearch.org/blog/2014-11-1-this-week-in-elasticsearch/
6. This week in elasticsearchNovember 26, 2014 http://www.elasticsearch.org/blog/2014-11-26-this-week-in-elasticsearch/
7. kibana 4 beta 2: get it now http://www.elasticsearch.org/blog/kibana-4-beta-2-get-now/
8. elasticsearch 1.4.1 and 1.3.6 released http://www.elasticsearch.org/blog/elasticsearch-1-4-1-released/


## TODO
*	http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/index-modules-allocation.html#disk
*	http://www.elasticsearch.org/blog/elasticsearch-1-4-1-released/中的parent/child and nested documents是什么意思
*	Want to learn more about testing automation for distributed applications? Isabel Drost-Fromm’s latest paper is a great place to start! Isabel will show you how we at Elasticsearch ensure quality checks are run often enough to speed up failure discovery, while still keeping the runtime of the whole test suite low enough for our developers to be able to run the test suite in their local development environment.
http://www.elasticsearch.org/blog/white-paper-testing-automation-for-distributed-applications/
*	[Deep dive into Aggregations](https://speakerdeck.com/bleskes/deep-dive-into-aggregations)
*	[Deep Dive into Faceting](https://speakerdeck.com/bleskes/deep-dive-into-faceting)
*	http://www.rittmanmead.com/2014/11/analytics-with-kibana-and-elasticsearch-through-hadoop-part-1-introduction/
*	http://www.rittmanmead.com/2014/11/analytics-with-kibana-and-elasticsearch-through-hadoop-part-2-getting-data-into-elasticsearch/
*	http://www.rittmanmead.com/2014/11/analytics-with-kibana-and-elasticsearch-through-hadoop-part-3-visualising-the-data-in-kibana/


> Written with [StackEdit](https://stackedit.io/).
