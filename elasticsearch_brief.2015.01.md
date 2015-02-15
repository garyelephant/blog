# Elasticsearch 2015年01月简报

---

## Elasticsearch Updates
这个月没什么大变化。
*	Dependencies: Upgrade to lucene-5.1.0-snapshot-1652032 ([#9318](https://github.com/elasticsearch/elasticsearch/pull/9318), 2.0.0)

*	Lucene: Expose auto-IO-throttle from Lucene’s ConcurrentMergeScheduler ([#9243](https://github.com/elasticsearch/elasticsearch/pull/9243), 2.0.0)

*	The [release branch for Lucene 5.0](https://svn.apache.org/repos/asf/lucene/dev/branches/lucene_solr_5_0/) was recently cut, and the committer team is busy preparing an RC and release. If you’re interested in all the new features upcoming in the 5.0 release, our very own [Mike McCandless has you covered](http://blog.mikemccandless.com/2014/11/apache-lucene-500-is-coming.html) or simply check out the [changes list](https://svn.apache.org/repos/asf/lucene/dev/branches/lucene_solr_5_0/lucene/CHANGES.txt).


## Elasticsearch Ecosystem Updates
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

*	William Durand gave a presentation on deploying a web application stack with Docker at the Clermont’ech API Hour in France last month. His follow-up blog post summarizes how he does the monitoring for that infrastructure – with the ELK stack, of course! – and includes some best practices for deploying the ELK stack with Docker.
http://williamdurand.fr/2014/12/17/elasticsearch-logstash-kibana-with-docker/

*	[video]Bhaskar Karambelkar of Verizon shared his tips on scaling Elasticsearch for production-scale data at the Washington, D.C. meetup on December 11.
http://pdl.vimeocdn.com/25240/756/322885542.mp4?token2=1423638543_1d903dc4e351379797caab75dc0a1d83&aksessionid=1d21f8f223594ab4

*	Google Compute Engine发布了Getting started with click-to-deploy Elasticsearch
https://cloud.google.com/solutions/elasticsearch/click-to-deploy

*	This great post from Njal Karevoll at Found is perfect for those of you getting started with Elasticsearch — giving an overview of the different client types available, and how to choose which to pick.
https://www.found.no/foundation/interfacing-elasticsearch-picking-client/

*	[video]At one the December gathering of the Elasticsearch London MeetUp group, Ian Plosker – CTO & Co-founder at Orchestrate.io – shared some great real-world lessons in his talk “Schemalessness Gone Wrong: Improving Elasticsearch with ‘Tuplewise Transform’”
http://pdl.vimeocdn.com/52957/092/317986514.mp4?token2=1423636182_132dac3a0f2134d94dd55cdee572dbcb&aksessionid=9863655acfe61d87

*	We love sharing our user’s success stories. Check out this post from the folks at TrackJS on how the scaled up their Elasticsearch infrastructure, ‘on a budget‘. You might also want to register for our upcoming webcast where the TrackJS will folks will give you even more detail on scaling Elasticsearch, fast!, for fun and profit.
The fine folks at TrackJS authored an in-depth guest blog post on their Elasticsearch use case, which is of particular interest given their resource constraints. Check out the article for more information, and details on how to register for our upcoming webcast with the TrackJS team.
http://www.elasticsearch.org/blog/scaling-trackjs-with-elasticsearch-for-fun-and-profit/

*	Nikos Fertakis shared an article on how Skroutz – a Greek price comparison website serving up details on more than 7.5M products – uses ELK to make their customers’ lives better. The entire deep dive is quite useful, but the infrastructure architecture bits and their use of scripted aggregations is particularly interesting.
http://engineering.skroutz.gr/blog/elk-at-skroutz/

*	Node Discovery in Cloud Environment
https://speakerdeck.com/elasticsearch/node-discovery-in-cloud-environment

*	Lucene’s handling of deleted documentsJanuary 30, 2015
http://www.elasticsearch.org/blog/lucenes-handling-of-deleted-documents/

*	Numeric Aggregations: An Exploration of UK Housing DataJanuary 29, 2015
http://www.elasticsearch.org/blog/numeric-aggregations-an-exploration-of-uk-housing-data/


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