# Logstash 优化笔记

---

## TODO

*	配置优化
*	logstash 性能优化
*	自动生成logstash conf的功能
*	logstash-filter-geoip2
*	用户日志格式设计规范的内容和意义

---

## logstash 配置常用技巧汇总

*	logstash-filter-grok使用技巧

---

0. 基本的配置方法，一定要先掌握这个
https://www.elastic.co/guide/en/logstash/current/configuration.html

3.
regex 中的(pattern)?表示这个pattern可能出现也可能不出现。


4.grok中最简单的自定义pattern方法
(?<field_name>the pattern here)

如，我们为ww2.sinaimg.cn:80，定义了一个patter (?<domain>%{IPORHOST}(:%{POSINT})?)


5.在这里debug grok
http://grokdebug.herokuapp.com/


6.如果你不保留raw 格式的event, 但是仍希望在_grokparsefailure时，可以查看raw event, 方便debug, 可以把logstash配置成这样：
`TODO`:这个代码的逻辑应该改成，如果出现grokfailure,再写_event_meta
input {
    stdin {}
}

filter {
    # you could configure like this:
    #mutate {
    #    add_field => { "[_event_meta][raw_msg]" => "%{message}" }
    #}

    # or like this:
    # get raw_msg, logstash_indexer(pid, ips) for debug
    ruby {
        code => "require 'socket'
                 field = '[_event_meta][raw_msg]'
                 field = event.sprintf(field)
                 event[field] = event['message']
                 field = '[_event_meta][logstash_indexer][pid]'
                 field = event.sprintf(field)
                 event[field] = Process.pid
                 # get AddrInfo array
                 field = '[_event_meta][logstash_indexer][ips]'
                 event[field] = []
                 Socket.ip_address_list.each do |ip_info|
                     if ip_info.ipv4? and !ip_info.ipv4_loopback?
                         event[field] << ip_info.ip_address
                     end
                 end
                "
    }

    # feel free to grok !!
    #grok { match => [ "...", "..."]}

    #...

    if [tags] {
        if ( "_grokparsefailure" not in [tags] ) and ( "_jsonparsefailure" not in [tags] ) {
            mutate {
                remove_field => [ "_event_meta" ]
            }
        }    
    }
    else {
        mutate {
            remove_field => [ "_event_meta" ]
        }
    }
}

output {
    stdout { codec => rubydebug }
}

输入：fffffffffffffffffffffffffffffffffffffffffffffff

输出如下：
{
        "message" => "fffffffffffffffffffffffffffffffffffffffffffffff",
       "@version" => "1",
     "@timestamp" => "2015-04-02T13:32:53.878Z",
           "host" => "gz187-65.sina.com.cn",
    "_event_meta" => {
                 "raw_msg" => "fffffffffffffffffffffffffffffffffffffffffffffff",
        "logstash_indexer" => {
            "pid" => 43333,
            "ips" => [
                [0] "172.16.187.65",
                [1] "183.60.187.65"
            ]
        }
    }
}


7.kafka input
input {
    kafka {
        topic_id => "www_sinastorekywm1fcines_load"
        group_id => "logstash_www_sinastorekywm1fcines_load"
        zk_connect => "10.13.80.21:2181,10.13.80.22:2181,10.13.80.23:2181/kafka/k1001"
        codec => "plain" # default codec is "json",默认把从kafka中获取到的message按json string解析, 如果不是json,换成其他codec, 否则会出现"_jsonparsefailure"
    }
}


8.
"tags"这个字段是logstash的保留字段，
"tags" => [
    [0] "_jsonparsefailure",
    [1] "_grokparsefailure"
    [2] "multiline"
]

9.logstash常用的插件 : date
date {
    match => ["timestamp", "date_format_of_timestamp"]
    target => "@timestamp"
}

date format 格式可以在这里查到：
http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html

10.处理某field时，应该先判断它是否存在
尤其是使用logstash-filter-ruby时。如果出错(如抛出异常,可能导致logstash停止工作或退出,而你全然不知)，它不会忘日志记录任何信息，除非在ruby code中加入相关的记录日志的代码。
filter {
    if [some_field] {
        ruby {
            # get last ip of event['some_field']
            code => "last_segment = event['somefield'].split('|')[-1]
                     event['new_field'] = last_segment.split(',')[0]"
        }
    }
}

即使待处理的field存在，也可能会因为不严谨的代码或其他filter处理不当导致ruby filter抛出异常(Exception in filterworker)，最终所有的ilterworker thread退出，logstash停止工作，所以，还是尽量不要用ruby filter。

再看另一个例子：

如果直接写：
```
    ruby {
        code => "
            event[ '_object' ].each { |k, v|
                event[ k ] = v
            }
            event.remove( '_object' )
        "
    }
```

在logstash-1.5.0中，会抛出异常，问题出在哪里？

```
Exception in filterworker {"exception"=>#<NoMethodError: undefined method `each' for nil:NilClass>, "backtrace"=>["(ruby filter code):2:in `register'", "org/jruby/RubyProc.java:271:in `call'", "/opt/logstash/vendor/bundle/jruby/1.9/gems/logstash-filter-ruby-0.1.5/lib/logstash/filters/ruby.rb:37:in `filter'", "/opt/logstash/vendor/bundle/jruby/1.9/gems/logstash-core-1.5.0-java/lib/logstash/filters/base.rb:162:in `multi_filter'", "org/jruby/RubyArray.java:1613:in `each'", "/opt/logstash/vendor/bundle/jruby/1.9/gems/logstash-core-1.5.0-java/lib/logstash/filters/base.rb:159:in `multi_filter'", "(eval):261:in `filter_func'", "/opt/logstash/vendor/bundle/jruby/1.9/gems/logstash-core-1.5.0-java/lib/logstash/pipeline.rb:219:in `filterworker'", "/opt/logstash/vendor/bundle/jruby/1.9/gems/logstash-core-1.5.0-java/lib/logstash/pipeline.rb:156:in `start_filters'"], :level=>:error}
```

所以我们要这么写：

```
# 在ruby filter中任何使用任何event field都要先判断它是否存在
    ruby {
        code => "
            if event[ '_object' ] != nil
                event[ '_object' ].each { |k, v|
                    event[ k ] = v
                }
                event.remove( '_object' )
            end
        "
    }

```


11.conditional if issuccess is true
if [issuccess] {
    ...
}
else {
    ...
}

12. conditional if some_field exists
if [some_field] {
    ...
}
如果要把某个field的值和其他值做比较，应先判断这个值是否存在，再做比较，如：

if [ver] and [ver] >= '5.5.0' {
    ...
}

否则对于`ver`不存在的event，logstash worker thread处理时将抛出异常，导致thread退出，logstash僵死。
相关issue见：https://github.com/elastic/logstash/issues/4138


13. Logstash-output-elasticsearch的error log信息不全导致查问题困难
Logstash 1.2.0以后对这个问题做了改进，如增加了常见的es返回的400错误的原因及indexing错误的数据，之前我们用logstash1.x.x版本的时候，发现这种错误日志后很难查问题，还需要找到原来的数据手工indexing看错误码和原因。
下面有几个相关的issues:
https://github.com/logstash-plugins/logstash-output-elasticsearch/issues/225

14.将Logstash Event中的所有字段的值全部转换为string,支持多层嵌套
```
# json example:{"k1":"3","k2":"4","k3":{"k4":2,"k5":[3,4],"k8":["ab","123"]},"k6":["sfsf","fsffs"],"k7":[23,22],"k10":null,"k11":[{"k12":true},{"k13":3}],"k14":[[1,2],["a","b"]]}

```
注意：这个函数iterate_hash无法处理两层及以上的array嵌套,如 [ [1,2] ], 将输出：[ "[1,2]" ]
```
    ruby {
        code => "
            def iterate_hash( h )
                # convert all values to string in place
                h.each do | k, v |
                    value = v

                    if value.is_a?( Hash )
                        iterate_hash( value )

                    elsif value.is_a?( Array )
                        h[ k ] = value.map { |a| a.is_a?(Hash) ? iterate_hash( a ) : a.to_s }

                    elsif value.is_a?( NilClass )
                        h[ k ] = 'nil'
                    else
                        h[ k ] = value.to_s
                    end
                end
            end

            data = event.to_hash

            iterate_hash( data )

            e = LogStash::Event.new( data )
            event.overwrite( e )
        "
    }
```

15. 如何把json转换为string

使用mutate的convert to string是不行的

```
    mutate {
        replace => [ "your_json_fieldname", "%{your_json_fieldname}" ]
    }
```

16. logstash 最常用的几个plugin:

> 如果要自己实现一个类似logstash的日志解析工具，实现了下面的plugins的功能就足够用了。

*   input

stdin, file, kafka, tcp, heartbeat,

*   filter

grok, json, date, mutate, ruby, prune, kv

prune: whitelist, blacklist on event
https://www.elastic.co/guide/en/logstash/current/plugins-filters-prune.html

*   output

elasticsearch,

17. 使用logstash处理格式不固定的日志（1）-- 日志前面格式相同，后面格式不相同
如下的日志，roomid之前的部分格式相同，后面不一样。
```
1.       2015-12-28 11:33:45.590 [info] <0.13300.0>@chatroom_handler:r_join:82 type:user_join_in_room,uid:2654836515, gdid:<<"chatroom:c0e868348e4e36665e1870d067797dd3:2654836515">>, from:<<"chatroom:c0e868348e4e36665e1870d067797dd3:2654836515">>, roomid:"2308623924987105936940", container_id:"2309163a0172da0f0e74b1427e394854dd47cf", count:4, status:1
2.       2015-12-28 11:32:50.113 [info] <0.13049.0>@chatroom_handler:r_join:82 type:user_join_in_room,uid:5662498887, gdid:<<"1d29805db9b5d786fa3ab4c6">>, from:<<"1057093010">>, roomid:"2308623924980793522371", container_id:"230916721fc8c5f7cb8aadec9f2c0808b3abcb", count:2, status:1
3.       2015-12-28 11:33:05.409 [info] <0.13102.0>@chatroom_handler:r_click:264 type:user_click,uid:5662498887, gdid:<<"1d29805db9b5d786fa3ab4c6">>, from:<<"1057093010">>, roomid:"2308623924980793522371", value:3
4.       2015-12-28 11:34:17.384 [info] <0.13397.0>@chatroom_handler:r_exit:180 type:exit_room,uid:5662498887, gdid:<<"1d29805db9b5d786fa3ab4c6">>, from:<<"1057093010">>, roomid:"2308623924980793522371", time:23
5.       2015-12-28 11:51:39.499 [info] <0.5286.1>@chatroom_handler:r_msg:211 type:user_msg,uid:5662498887, gdid:<<"1d29805db9b5d786fa3ab4c6">>, from:<<"1057093010">>, roomid:"2308623924980793522371"
```

后面不一样的部分，为了简化配置，使其可读性，扩展性更好，可以配置如下：
```
# 用extras匹配后半部分，之后再根据不同情况解析extras

filter {
    grok {
        match => {
            "message" => [ "%{DATA:timestamp} \[%{LOGLEVEL:log_level}\] %{DATA:undefined}@%{IP:ip} <%{DATA:undefined}>@chatroom_handler:\w+:\w+ type:%{DATA:type}, uid:
%{NUMBER:uid}, gdid:<<%{QS:gdid}>>, from:<<%{QS:from}>>, roomid:%{QS:roomid}(, %{DATA:extras})?$" ]
        }
    }

    if [type] {
        if [type] == "user_join_in_room" {
            grok {
                match => {
                    "extras" => [ "container_id:%{QS:container_id}, count:%{NUMBER:count}, status:%{NUMBER:status}" ]
                }
            }

            if [count] {
                mutate {
                    convert => {
                        "count" => "integer"
                    }

                }
            }
        }
        else if [type]=="user_click" {
            grok {
                match => {
                    "extras" => [ "value:%{NUMBER:value}" ]
                }
            }
        }
        else if [type]=="exit_room" {
            grok {
                match => {
                    "extras" => [ "time:%{NUMBER:time}" ]
                }
            }
        }
        else if [type]=="user_msg" {
            # don't need to do anything
        }

        mutate {
            remove_field => [ "extras" ]
        }
    }

    ...
}
```



90.如何在logstash中使用java
puts event # event references
puts event['message'] # message of event
puts "Some: #{value}" # value is a variable
require 'java' # jruby calling java from jruby, after java imported , you can use java libraries


99.尽可能不要在conf中使用logstash-filter-ruby, 很容易出错，bin/logstash -t 检查不出ruby code的错误，错误不会记日志，debug困难, 甚至可能导致OOM

100.一些可能用到的ruby 技巧
#get type of a variable
>> "string".class
=> String
>> [1,2,3].class
=> Array
http://stackoverflow.com/questions/15769739/determining-type-of-an-object-in-ruby

# puts, print

101.What is the purpose of the question mark operator in Ruby?

Sometimes it appears like this:

assert !product.valid?
sometimes it's in an if construct.
Answer:
It is a code style convention; it indicates that a method returns a boolean value.

The question mark is a valid character at the end of a method name.

102.A Beginner’s Guide To Ruby
https://hackhands.com/beginners-guide-ruby/

How do I introspect things in Ruby?
http://stackoverflow.com/questions/2492730/how-do-i-introspect-things-in-ruby

string split
http://www.dotnetperls.com/split-ruby

string trim:
" Raheem Shaik ".strip
http://stackoverflow.com/questions/1634750/ruby-function-to-remove-all-white-spaces

array slicing
http://stackoverflow.com/questions/695290/how-to-return-a-part-of-an-array-in-ruby

Ruby combining(join) an array into one string
http://stackoverflow.com/questions/4018689/ruby-combining-an-array-into-one-string

@ in object:
These are variables whose scope is limited to one particular instance of a class. They are defined with @ at the beginning of the name of the variable.

103. determining type of an object in ruby
s1 = {"k1" => "v2", "k2" => "v2" }
puts s1.is_a?(Hash)

s2 = "fsfsfsf"
puts s2.is_a?(String)


104. logstash-filter-ruby中使用event
event是Logstash::Event的实例，从logstash 源码[event.rb](https://github.com/elastic/logstash/blob/master/logstash-core-event/lib/logstash/event.rb)可以看到它的用法

get and set:
var1 = event['message']
event['message'] = var2



---

> Written with [StackEdit](https://stackedit.io/).