
# Elasticsearch 2015年02月简报

---

## Elasticsearch Updates


## Elasticsearch Ecosystem Updates
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

5.	Elasticsearch 1.4.3 and 1.3.8 releasedFebruary 11, 2015
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

12.	Shield 1.0.1 releasedFebruary 13, 2015
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