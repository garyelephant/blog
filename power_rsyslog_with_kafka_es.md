# Tutorial: 使用rsyslog向kafka, elasticsearch推送日志

> 本文介绍了一种简单易行的使用rsyslog向kafka,elasticsearch推送日志的方法；rsyslog的omkafka插件的安装、使用方法；rsyslog的omelasticsearch插件的安装、使用方法。

Kafka是一种开源的分布式消息系统，项目主页：kafka.apache.org
elasticsearch是一种开源的分布式搜索引擎，项目主页：elastic.co

rsyslog使用omkafka向kafka推送日志，使用omelasticsearch向elasticsearch推送日志。这两个插件默认编译选项是关闭的，没有被编译到rsyslog中。下面介绍了具体的安装方法：

```
## add rsyslog repo
WORK_DIR=$(pwd)
cd /etc/yum.repos.d
wget http://rpms.adiscon.com/v8-stable/rsyslog.repo -O rsyslog.repo

cd $WORK_DIR
mkdir rsyslog-install
cd rsyslog-install

# check rsyslog version
# rsyslog supports kafka from v8.7.0
old_rsyslog_ver=$(rsyslogd -version |head -n 1 | awk '{print $2}')

## install rsyslog dependency: libestr
yum install -y libestr-devel

## install rsyslog dependency: libee
yum install -y libee-devel

## install rsyslog dependency: json-c
yum install -y json-c-devel

## install rsyslog denpendency: uuid
yum install -y libuuid-devel

## install rsyslog denpendency: liblogging-stdlog
yum install -y liblogging-devel

## install rsyslog denpendency: rst2man
yum install -y python-docutils

## install libcurl for omelasticsearch
yum install -y libcurl-devel

## install librdkafka for omkafka
wget https://github.com/edenhill/librdkafka/archive/0.8.5.tar.gz -O librdkafka-0.8.5.tar.gz
tar zxvf librdkafka-0.8.5.tar.gz
cd librdkafka-0.8.5
./configure
make
make install

cd ..
## install rsyslog
wget http://www.rsyslog.com/files/download/rsyslog/rsyslog-8.8.0.tar.gz -O rsyslog-8.8.0.tar.gz
tar zxvf rsyslog-8.8.0.tar.gz
export PKG_CONFIG_PATH=/usr/lib64/pkgconfig:/lib64/pkgconfig/
old_executable_path=$(which rsyslogd)
executable_dir=$(dirname "$old_executable_path")
cd rsyslog-8.8.0
./configure --sbindir=$executable_dir --libdir=/usr/lib64 --enable-omkafka --enable-elasticsearch
make
make install

## show installation result:
new_rsyslog_ver=$(rsyslogd -version |head -n 1 | awk '{print $2}')
echo "Old rsyslogd version: "$old_rsyslog_ver
echo "New rsyslogd version: "$new_rsyslog_ver
echo "Executable: " $(which rsyslogd)

```

我在Github上托管了相关代码：
https://github.com/garyelephant/rsyslog-scripts

omkafka插件的详细文档见：
http://www.rsyslog.com/doc/master/configuration/modules/omkafka.html

omelasticsearch插件的详细文档见：
http://www.rsyslog.com/doc/v8-stable/configuration/modules/omelasticsearch.html

## 配置示例：
```
# /etc/rsyslog.conf
# load required module
# `imuxsock` provides support for local system logging (e.g. via logger command)
module(load="imuxsock") 
module(load="omkafka")
module(load="omelasticsearch")

# push to kafka
action(type="omkafka" topic="your_topic" broker="your_kafka_broker_host_or_ip")

# or you can push to elasticsearch
action(type="omelasticsearch" server="your_elasticsearch_host_or_ip" searchIndex="your_elasticsearch_index" searchType="your_elasticsearch_index_type" )
```

启动 rsyslog
```
rsyslogd -n
```
在另一个终端用`logger`向rsyslog写数据
```
$ logger 'hello world'
```

## References:
1.	http://www.rsyslog.com/doc/master/installation/install_from_source.html
2.	http://bigbo.github.io/pages/2015/01/21/syslog_kafka/
3.	http://blog.oldzee.com/?tag=rsyslog
4.	http://www.rsyslog.com/newbie-guide-to-rsyslog/
5.	http://www.rsyslog.com/doc/master/configuration/modules/omkafka.html

---

转载本文请注明作者和出处[Gary的影响力]http://garyelephant.me，请勿用于任何商业用途！
Author: Gary Gao( garygaowork[at]gmail.com) 关注互联网、分布式、高性能、NoSQL

> Written with [StackEdit](https://stackedit.io/).