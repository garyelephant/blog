# Elasticsearch Brief 2014年10月

## Elasticsearch Updates
*	发布了Kibana 4 Beta 1 和Beta 1.1。
Kibana 4无论是在界面的布局，使用配置方法，还是底层绘制图表的方式都与Kibana不同。在Kibana 3的基础上吸取了众多社区的功能需求后，Kibana自Kibana 2 大改造成Kibana 3 后第二次做出了重大改变。Kibana真是一直致力于帮助用户解决他们在数据可视化上的棘手问题。
	界面由原来的一个`Dashboard`，改为现在的`Discover`, `Visualize`, `Dashboard`三个Tab，再加上`Settings`总共4个不同的Tab。

	*	`Discover`:这个Tab的界面是不是与以前的Kibana 2 很像？面向index的查询，即搜索index内容。搜索框中可以输入`Lucene Query String syntax`或者es的`json格式的query`,而且现在query不在仅仅属于某个dashboard，现在是全局共享的,而且可以通过URL传入，链接到某个query变得非常简单。
![Kibana 4 Discover Tab](https://github.com/garyelephant/blog/blob/master/images/elasticsearch_brief_2014.10_1.png)

	* `Visualize`:可以使用es的`aggregations`做逻辑复杂多样化的图表。(kibana3使用的es的facet,aggregations比它功能多，更复杂)，点击visualize底部的灰色可以直接看到图表的原始数据，request,response和请求处理时间等相关统计。
![Kibana 4 Visualize Tab](https://github.com/garyelephant/blog/blob/master/images/elasticsearch_brief_2014.10_2.png)

	* `Dashboard`:Dashboard还是用来创建一个图表集的，满足特定的一类可视化需求，但是它比以前更容易配置和维护。显而易见，Kibana 4大大增加了图表和query的可重用性。在`Visualize`中创建的图表可以在`Dashboard`中重用多次。现在，一个Dashboard还可以展示多个index的数据。
![Kibana 4 Dashboard Tab](https://github.com/garyelephant/blog/blob/master/images/elasticsearch_brief_2014.10_dashboard.png)

	* `Settings`:kibana的一些全局设置

>注意：Kibana 3与Kibana 4的schema不兼容，Kibana 3的配置不能导入到Kibana 4中。Kibana 4需要Elasticsearch的版本 >= 1.4.0

*	 发布了Elasticsearch 1.4.0.Beta1
这个版本的主要在稳定性和可靠性上做了改进。

	* Better node stability through reduced memory usage.
对最近引入的doc value机制做了大幅改进，用来替换原来的in memory fielddata。doc value是原来存在内存中用来做聚合，统计，查询的字段的值存在磁盘上，利用 系统内核的filesystem cache来加速对doc value的访问，使性能接近原来的fielddata。
增加了对处理单个请求可占用的内存的限制(request circuit breaker)。

	* Better cluster stability through improved discovery algorithms.
修复了诸多用户在生产环境中遇到的集群不稳定的问题。并在[resiliency status][4]详细列出了用户提交的相关问题及它们的修复进度和在生产环境中保护数据的措施。

	* Better detection of corrupted data through checksums.
在shard recovery, merging, transaction log等多处加入Checksums 验证功能来验证数据是否损坏。
	* 其他主要更新
[groovy替换了mvel][5]成为ES默认的脚本语言来提高安全性和运行效率。
处于安全性考虑，跨域访问改为默认关闭。新增了3种aggregations类型：[filters](http://www.elasticsearch.org/guide/en/elasticsearch/reference/1.4/search-aggregations-bucket-filters-aggregation.html), [children](http://www.elasticsearch.org/guide/en/elasticsearch/reference/1.4/search-aggregations-bucket-children-aggregation.html), [scripted_metric](http://www.elasticsearch.org/guide/en/elasticsearch/reference/1.4/search-aggregations-metrics-scripted-metric-aggregation.html)。随着ES中集成的Lucene版本的不断更新，以后的ES版本中将逐渐不在支持Lucene 3.x的index,所以ES新增了your_index/_upgrade REST API用以将老旧的index转换为兼容最新Lucene的index.

## Elasitcsearch Ecosystem Updates
*	发布了Elasticsearch Hadoop 2.0.2 and 2.1.Beta2[TODO]


## Amazing Slides & tutorials &  videos
*	[playing http tricks with nginx][11]
使用nginx来做es的proxy,提供持久http链接，load balance, security control（basic http auth, role based auth,oauth)功能
*	[deploying the ELK stack using Docker][12]
用时下流行的app容器docker部署ELK
*	[Elasticsearch from the Top Down Tracing a Request Down to the Bits][13]
从Elasticsearch实现底层讨论了ES集群处理index ,query请求的过程。
*	[Building Scalable Search from Scratch with ElasticSearch][14]



## Meetups in China
*	10月25日，第三届elasticsearch国内开发者交流大会。详细信息：http://www.meetup.com/Elasticsearch-China-Users/events/210253352/。
大会PPT下载：http://pan.baidu.com/s/1i3qsoBF


[1]: http://www.elasticsearch.org/blog/kibana-4-beta-1-released/ "Kibana 4 Beta 1 released"
[2]: http://www.elasticsearch.org/blog/kibana-4-beta-1-1-pointy-needles-blunted/ "kibana 4 beta 1.1: pointy needles blunted "
[3]: http://www.elasticsearch.org/blog/elasticsearch-1-4-0-beta-released/ "Elasticsearch 1.4.0.Beta1 released"
[4]: http://www.elasticsearch.org/guide/en/elasticsearch/resiliency/current/index.html "resiliency status"
[5]: http://www.elasticsearch.org/blog/scripting/ "all about scripting"
[6]: http://www.elasticsearch.org/blog/elasticsearch-hadoop-2-0-2-and-2-1-beta2/ "Elasticsearch Hadoop 2.0.2 and 2.1.Beta2 released"
[7]: http://www.elasticsearch.org/blog/2014-10-08-this-week-in-elasticsearch/ "This week in Elasticsearch October 8, 2014"
[8]: http://www.elasticsearch.org/blog/2014-10-15-this-week-in-elasticsearch/ "This week in Elasticsearch October 15, 2014"
[9]: http://www.elasticsearch.org/blog/2014-10-22-this-week-in-elasticsearch/ "This Week in ElasticsearchOctober 22, 2014"
[10]: http://www.elasticsearch.org/blog/2014-10-29-this-week-in-elasticsearch/ "This week in ElasticsearchOctober 29, 2014"
[11]: http://www.elasticsearch.org/blog/playing-http-tricks-nginx/ "playing http tricks with nginx"
[12]: https://clusterhq.com/blog/deploying-multi-node-elasticsearch-logstash-kibana-cluster-using-docker/ "deploying the ELK stack using Docker"
[13]: https://found.no/foundation/elasticsearch-top-down/ "Elasticsearch from the Top Down Tracing a Request Down to the Bits"
[14]: http://www.airpair.com/elasticsearch/posts/elasticsearch-robust-search-functionality "Building Scalable Search from Scratch with ElasticSearch"

---
[TODO]
*   [elasticsearch testing & qa: elasticsearch continuous integration](http://www.elasticsearch.org/blog/elasticsearch-testing-qa-elasticsearch-continuous-integration/)
*   [elasticsearch testing & qa: testing levels of elasticsearch](http://www.elasticsearch.org/blog/elasticsearch-testing-qa-testing-levels-elasticsearch/)
*   [elasticsearch testing and qa: increasing coverage by randomizing test runs](http://www.elasticsearch.org/blog/elasticsearch-testing-qa-increasing-coverage-randomizing-test-runs/)