
# Elasticsearch 2015年02月简报

---

## Elasticsearch Updates
*	Elasticsearch 1.4.3 and 1.3.8 released
	*    Security:Disable dynamic Groovy scripting by marking Groovy as not sandboxed. [#9655](https://github.com/elastic/elasticsearch/issues/9655)
	*     Discovery: publishing timeout to log at WARN and indicate pending nodes [#9551](http://github.com/elasticsearch/elasticsearch/issues/9551)
	*     THESE RELEASES FIX A VULNERABILITY IN SCRIPTING. WE ADVISE ALL USERS TO UPGRADE.
	*    Groovy scripting vulnerability found
现在的问题：Elasticsearch versions 1.3.0-1.3.7 and 1.4.0-1.4.2，The vulnerability allows an attacker to construct Groovy scripts that escape the sandbox and execute shell commands as the user running the Elasticsearch Java VM.Versions 1.3.8 and 1.4.3 disable sandboxing for Groovy by default. As a consequence, dynamic script execution is disabled for Groovy.In the meantime, you can still use Groovy scripts by saving them as files in the config/scripts directory on every data node. See [Running scripts without dynamic scripting](http://www.elasticsearch.org/blog/running-groovy-scripts-without-dynamic-scripting/) for more information about how to do this.
将来的计划：
Unfortunately, after discussing the issue with the Groovy team, we have come to the conclusion that the Groovy language is too dynamic to be properly contained by a sandbox. This leaves us with the [Lucene Expressions language](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/modules-scripting.html#_lucene_expressions_scripts) as the only dynamic scripting language available by default. While Expressions are fast, they are currently very limited: they operate only on numeric fields and don't support loops.We will be investigating extending Expressions to become a more powerful (but safe!) mini-language, that will support at least the most common use cases that our script users have today.


release not & download: https://www.elastic.co/downloads/past-releases/1-4-3 , https://www.elastic.co/downloads/past-releases/1-3-8

## Elasticsearch Ecosystem Updates
> Kibana 4是本月的主题！！

*	kibana 4
专门花了2小时时间去研究了一下kibana4相对kibana3的变化，界面较3有较大改动，据说越来越像`splunk` ? 互相借鉴嘛，取长补短，挺好的。我总结了下自己觉得眼前一亮的功能：
	*    在`Discover` Tab中搜索数据，被搜索到的字段值自动高亮显示。

	*    kibana 4使用了强大的`aggregations`, 这意味着通过使用多层嵌套的aggs查询得到的数据可以画出表达更直接，更贴近数据可视化需求的图表。在kibana3中大部分想到做不到的，现在只要你能想到。。。

	*    `Visualize`在配置的灵活性上做了很大调整，可生成丰富的图表。这与`aggregations`有很大关系。

	*    可以分享某个`Visualization`(图表)的链接，或者把它嵌入到其他页面中。

	*    `Dashboard`中，可以自由得拖曳、放大、缩小图表。

	*    可以跨index。

	*    search, filter, 图表的参数可以通过url指定。

每当我想到elasticsearch,kibana,logstash的时候，总会不由得发出感叹：“像这种盈利性公司主导的开源社会，他们做的开源产品简直太棒了！”

## Amazing Slides & tutorials & videos
*	Florian Hopf authored an article on Fixing Elasticsearch Allocation Issues he encountered while working with 350 Logstash indices on his laptop. Nice post on the process of debugging, how the Cluster Stats API can make your life easier.
http://blog.florian-hopf.de/2015/02/fixing-elasticsearch-allocation-issues.html

*	Steve Elliott with the LateRooms engineering team wrote up a how to on analyzing URLs to enrich your logs for users of Logstash 1.4.x. Offers great tips on using the Grok and Translate plugins, amongst other useful bits. If you enjoyed Steve’s post, you may also want to take a look at how LateRooms uses the full ELK stack to drive data driven decision making for every department at their company. That’s right, Data Driven Managering.
http://engineering.laterooms.com/enriching-logs-with-logstash/
http://engineering.laterooms.com/elks-in-laterooms/

*	Nick Canzoneri with Postmark published an article about how they’ve revisited their Elasticsearch architecture to handle the ever increasing volumes of data that come with scaling your business. Even better, he’s offered to answer your scaling questions if you leave comments on his post. Excellent overview of architectural considerations from a long time happy user.
http://blog.postmarkapp.com/post/109309498178/were-doubling-down-on-elasticsearch

*	Capacity Planning and Custom Setups Suitable for Large Elasticsearch Deployments
https://speakerdeck.com/elasticsearch/not-all-nodes-are-created-equal-scaling-elasticsearch-1

*	Christoffer Vig from our partner firm, Comperio, shared an awesome walk through post on analytics with Elasticsearch and Kibana 4. In his post, you’ll learn all about how to use the two together to gain valuable insights, such as “Which Belgian Beer gives you the most value for the money?”
http://blog.comperiosearch.com/blog/2015/02/09/kibana-4-beer-analytics-engine/

*	Marco Bonzanini shared an article exploring some options to improve the results of Elasticsearch queries with multiple terms. Amongst other use cases in this post, you’ll learn about phrase-based matches and phrase matches with slop for proximity search.
http://marcobonzanini.com/2015/02/09/phrase-match-and-proximity-search-in-elasticsearch/

*	Alexander Reelsen’s quick introduction to Elasticsearch’s percolator, showcasing the potential of performing document enrichment before indexing
https://speakerdeck.com/elasticsearch/using-the-percolator-for-simple-classification

*	If you’re using Apache Hadoop and Spark, you won’t want to miss this post from Avi Levi on using the ELK stack for setting up a central logging infrastructure.
http://tech-stories.com/2015/02/12/setting-up-a-central-logging-infrastructure-for-hadoop-and-spark/

*	Interested in alerting for your website? Elasticsearch’s Percolator feature is your friend! Fabio Ponciroli wrote up how he and his colleagues added this functionality to their infrastructure at their company’s recent hack day.
http://http//techblog.net-a-porter.com/2015/02/perl-and-the-elasticsearch-percolator/

*	Elasticsearch, Logstash and Kibana on Docker
http://raulcd.com/elasticsearch-logstash-and-kibana-on-docker.html

*	As part of our ongoing guest blogger series, Oliver Eilhard shared the story of how Elasticsearch made his auto racing team faster. (We’re also always on the look out for amazing posts like Oliver’s, so if you enjoyed the piece and are inspired to share your story, please email us at stories@elasticsearch.com.)
http://www.elasticsearch.org/blog/how-elasticsearch-made-us-faster-literally/

*	Alex Brasetvik authored a blog post on common use cases for Elasticsearch. Excellent resource if you’re just starting out using it.
https://www.found.no/foundation/uses-of-elasticsearch/

*	Javier Ray from Tryolabs published a deep dive on Elasticsearch Analyzers as part of the lead up to Elastic{ON}. (And many thanks to Tryolabs for sponsoring our first ever User Conference!
http://blog.tryolabs.com/2015/02/25/elasticsearch-analyzers-or-how-i-learned-to-stop-worrying-and-love-custom-filters/

*    Ed King authored a great in-depth tutorial on integrating the ELK stack with Cloud Foundry.
http://www.cloudcredo.com/how-to-integrate-elasticsearch-logstash-and-kibana-elk-with-cloud-foundry/

*	The Luminis Engineering team authored a lovely how to on using the ELK stack to detect potential attacks on your WordPress blogs. Great step by step how to, including all needed configs for Logstash (v 1.5).
http://amsterdam.luminis.eu/2015/02/24/finding-your-blog-abusers-using-kibana-4-and-logstash-1-5/

*	Data Exploration with Elasticsearch
http://www.slideshare.net/astensby/data-exploration-with-elasticsearch?ref=http://www.elasticsearch.org/blog/2015-02-25-this-week-in-elasticsearch/

*	An introduction to Logstash and its ecosystem.
https://speakerdeck.com/purbon/logstash-the-shipper-with-a-moustasche

*	Pablo Figue’s presentation from last week’s Elasticsearch Berlin User Group meeting
https://speakerdeck.com/pfigue/how-do-we-use-logstash

*	https://relayr.io/ 物联网网站？

*	https://www.found.no/documentation/tutorials/using-java-transport/
Found.no开发的安全插件：Authentication，SSL encryption，Cluster handshake

*	https://speakerdeck.com/willdurand/docker-ceci-nest-pas-une-introduction-apihour-number-12

*	https://www.found.no/documentation/security/security-checklist/

*	https://www.found.no/documentation/security/access-control/

Understanding the Memory Pressure Indicator
*	https://www.found.no/foundation/memory-pressure/

## Meetups in China


##References
1.	This week in ElasticsearchFebruary 4, 2015
http://www.elasticsearch.org/blog/2015-02-04-this-week-in-elasticsearch/

2.	This week in ElasticsearchFebruary 11, 2015
http://www.elasticsearch.org/blog/2015-02-11-this-week-in-elasticsearch/

3.	This week in ElasticsearchFebruary 18, 2015
http://www.elasticsearch.org/blog/2015-02-18-this-week-in-elasticsearch/

4.	This Week in ElasticsearchFebruary 25, 2015
http://www.elasticsearch.org/blog/2015-02-25-this-week-in-elasticsearch/

5.	Elasticsearch 1.4.3 and 1.3.8 released
http://www.elasticsearch.org/blog/elasticsearch-1-4-3-and-1-3-8-released/

6.	elasticsearch 1.4.4 and 1.3.9 released
http://www.elasticsearch.org/blog/elasticsearch-1-4-4-and-1-3-9-released/

7.	Kibana 4 RC1 is freshly bakedFebruary 12, 2015
http://www.elasticsearch.org/blog/kibana-4-rc1-is-now-available/

8. Kibana 4. Literally.
http://www.elasticsearch.org/blog/kibana-4-literally/

9.	Kibana, aggregation execution order, and you
http://www.elasticsearch.org/blog/kibana-aggregation-execution-order-and-you/

10.	Kibana 4 for investigating PACs, Super PACs, and who your neighbor might be voting for
http://www.elasticsearch.org/blog/kibana-4-for-investigating-pacs-super-pacs-and-your-neighbors/

11.	Running Groovy Scripts without Dynamic ScriptingFebruary 11, 2015
http://www.elasticsearch.org/blog/running-groovy-scripts-without-dynamic-scripting/

12.	Shield 1.0.1 released
http://www.elasticsearch.org/blog/shield-1-0-1-released/

13.	Elasticsearch Puppet module 0.9.0 released
http://www.elasticsearch.org/blog/elasticsearch-puppet-module-0-9-0-released/

14.	Frame Of Reference and Roaring bitmaps
http://www.elasticsearch.org/blog/frame-of-reference-and-roaring-bitmaps/

15.	Highlights from Configuration Management Camp & AnsibleFest London
http://www.elasticsearch.org/blog/highlights-cfgmgmtcamp-ansiblefest/

16. Spotting Bad Actors: What Your Logs Can Tell You About Protecting Your Business
http://www.elasticsearch.org/blog/spotting-bad-actors-what-your-logs-can-tell-you-about-protecting-your-business/

17.	How Elasticsearch Made Us Faster – Literally
http://www.elasticsearch.org/blog/how-elasticsearch-made-us-faster-literally/

18.	Highlights from Southern California Linux Expo
http://www.elasticsearch.org/blog/highlights-from-scale/

19.	Behind the Antlers: Life Lessons from the Elastic{ON} CFP
http://www.elasticsearch.org/blog/behind-the-antlers-life-lessons-from-the-elasticon-cfp/

20.	[video]Kibana 4 video tutorials, Part 1
http://www.elasticsearch.org/blog/kibana-4-video-tutorials-part-1/

> Written with [StackEdit](https://stackedit.io/).