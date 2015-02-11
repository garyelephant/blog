# Elasticsearch 2015年01月简报

---

## Elasticsearch Updates
*	Dependencies: Upgrade to lucene 5 r1650327 [#9206](https://github.com/elasticsearch/elasticsearch/pull/9206)
*	Recovery: Be more resilient to partial network partitions ([#8720](https://github.com/elasticsearch/elasticsearch/pull/8720), 2.0.0, 1.5.0)
*	Aggregations: Add aimplifications ([#9097](https://github.com/elasticsearch/elasticsearch/pull/9097), 2.0.0)
*	

## Elasticsearch Ecosystem Updates


## Amazing Slides & tutorials & videos
*	Want more Python goodness? The folks at ClusterHQ have been hard at work on a project called Eliot, a structured logging system that can help you trace actions inside your processes. Check out their blog post on using the ELK stack to analyze logs, and how they have enabled cross-process logging
https://clusterhq.com/blog/eliot-0-6-logging-distributed-systems-python/

*	William Durand gave a presentation on deploying a web application stack with Docker at the Clermont’ech API Hour in France last month. His follow-up blog post summarizes how he does the monitoring for that infrastructure – with the ELK stack, of course! – and includes some best practices for deploying the ELK stack with Docker.
http://williamdurand.fr/2014/12/17/elasticsearch-logstash-kibana-with-docker/

*	Bhaskar Karambelkar of Verizon shared his tips on scaling Elasticsearch for production-scale data at the Washington, D.C. meetup on December 11.
http://pdl.vimeocdn.com/25240/756/322885542.mp4?token2=1423638543_1d903dc4e351379797caab75dc0a1d83&aksessionid=1d21f8f223594ab4

*	Peter Kim shares his tips on figuring out the amount of disk required for an Elasticsearch deployment.
http://peter.mistermoo.com/2015/01/05/hardware-sizing-or-how-many-servers-do-i-really-need/

*	If you’re a fan of Google Compute Engine, you’ll be thrilled to hear that Google has announced the release of Click to Deploy for Elasticsearch on GCE. It’s a great way to set up an Elasticsearch cluster, configured as you’d like, in just a few clicks.
https://cloud.google.com/solutions/elasticsearch/click-to-deploy

*	Yuriy Gerasimov has a guide for centralizing logs with Logstash — and doing so using pre-built Docker images, great for developers wanting to get started quickly.
http://ygerasimov.com/centralize-your-logs-with-logstash

*	Users of the Apache Camel Elasticsearch component will love this post on simplifying index management from Umberto Nicoletti.
http://unicolet.blogspot.it/2015/01/camel-elasticsearch-create-timestamped.html

*	This great post from Njal Karevoll at Found is perfect for those of you getting started with Elasticsearch — giving an overview of the different client types available, and how to choose which to pick.
https://www.found.no/foundation/interfacing-elasticsearch-picking-client/

*	[video]At one the December gathering of the Elasticsearch London MeetUp group, Ian Plosker – CTO & Co-founder at Orchestrate.io – shared some great real-world lessons in his talk “Schemalessness Gone Wrong: Improving Elasticsearch with ‘Tuplewise Transform’”
http://pdl.vimeocdn.com/52957/092/317986514.mp4?token2=1423636182_132dac3a0f2134d94dd55cdee572dbcb&aksessionid=9863655acfe61d87

*		

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