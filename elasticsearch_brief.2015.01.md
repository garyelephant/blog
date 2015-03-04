# Elasticsearch 2015年01月简报

---

## Elasticsearch Updates
这个月没什么大变化。

*	Lucene版本更新到了5.1.0

## Elasticsearch Ecosystem Updates
*	Lucene 5.0 即将发布，主要变化是保护index防止其损坏，减少对JVM Heap的占用。Lucene的核心开发者写了篇相关的博文:[Apache Lucene™ 5.0.0 is coming!](http://blog.mikemccandless.com/2014/11/apache-lucene-500-is-coming.html)

*	kibana4源码库merge了nodejs分支，从此kibana4的server端从JRuby改向nodejs了。(借用微博id:@argv的总结)

*	NEST & Elasticsearch .NET 1.4.
https://www.elasticsearch.org/blog/nest-1-4-released/
NEST 1.3到1.4的主要变化是bug fix和提供elasticsearch 1.4新增的功能，如 filters, children ,scripted metric aggregations。

*	The first GA release of Shield神盾局来了:
http://www.elasticsearch.org/blog/you-know-for-security-shield-goes-ga/


## Amazing Slides & tutorials & videos
*	  拥有强大统计，分析功能的Aggregations介绍上篇 from Zachary Tong
http://www.elasticsearch.org/blog/intro-to-aggregations/

*	Zachary Tong介绍Aggregations的第二篇，使用嵌套的aggregations满足多维度，复杂的分析需求。
http://www.elasticsearch.org/blog/intro-to-aggregations-pt-2-sub-aggregations/

*	Numeric Aggregations: An Exploration of UK Housing Data
本月介绍Aggregations的第三篇
http://www.elasticsearch.org/blog/numeric-aggregations-an-exploration-of-uk-housing-data/

*	使用Docker部署ELK
http://williamdurand.fr/2014/12/17/elasticsearch-logstash-kibana-with-docker/

*   如何选择es client. PS: found.no的blog是我常去的地方。
https://www.found.no/foundation/interfacing-elasticsearch-picking-client/

*	一个希腊的一个价格比较网站（Skroutz.gr）如何使用Elasticsearch作为分析平台
http://engineering.skroutz.gr/blog/elk-at-skroutz/

*	Lucene’s handling of deleted documents
介绍Lucene中的deleted documents
http://www.elasticsearch.org/blog/lucenes-handling-of-deleted-documents/

*	[video] Scaling Elasticsearch in a Production System
http://www.elasticsearch.org/videos/washington-d-c-meetup-december-11-2014/


## Meetups in China
*	Nothing


##References
*	This Week in ElasticsearchJanuary 7, 2015
http://www.elasticsearch.org/blog/2015-01-07-this-week-in-elasticsearch/

*	This Week in ElasticsearchJanuary 14, 2015
http://www.elasticsearch.org/blog/2015-01-14-this-week-in-elasticsearch/

*	This Week in ElasticsearchJanuary 21, 2015
http://www.elasticsearch.org/blog/2015-01-21-this-week-in-elasticsearch/

*	This week in ElasticsearchJanuary 28, 2015
http://www.elasticsearch.org/blog/2015-01-28this-week-in-elasticsearch/

*	Google Cloud Platform Delivers Real-Time Search with Click-to-Deploy Elasticsearch
http://www.elasticsearch.org/blog/google-cloud-platform-delivers-real-time-search-with-click-to-deploy-elasticsearch/

*	Intro to AggregationsJanuary 13, 2015
http://www.elasticsearch.org/blog/intro-to-aggregations/

*	Intro to Aggregations pt. 2: Sub-AggregationsJanuary 22, 2015
http://www.elasticsearch.org/blog/intro-to-aggregations-pt-2-sub-aggregations/

*	Numeric Aggregations: An Exploration of UK Housing DataJanuary 29, 2015
http://www.elasticsearch.org/blog/numeric-aggregations-an-exploration-of-uk-housing-data/

*	Scaling TrackJS with Elasticsearch for Fun and Profit
http://www.elasticsearch.org/blog/scaling-trackjs-with-elasticsearch-for-fun-and-profit/

*	You Know, for Security: Shield Goes GAJanuary 27, 2015
http://www.elasticsearch.org/blog/you-know-for-security-shield-goes-ga/

*	NEST 1.4 releasedJanuary 28, 2015
http://www.elasticsearch.org/blog/nest-1-4-released/

*	Lucene’s handling of deleted documentsJanuary 30, 2015
http://www.elasticsearch.org/blog/lucenes-handling-of-deleted-documents/


> Written with [StackEdit](https://stackedit.io/).