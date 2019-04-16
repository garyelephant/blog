## 数据仓库理论

###  数据库理论

* ER关系

https://www.cnblogs.com/muchen/p/5265305.html

* 第一范式(1NF), 第二范式(2NF)，第三范式(3NF)

http://www.cnblogs.com/muchen/p/5272620.html

https://beginnersbook.com/2015/05/normalization-in-dbms/

https://www.guru99.com/database-normalization.html

```
# 结论： 

1NF: Only one value per column

2NF: All the non primary key columns in the table should depend on the entire primary key.

3NF: All the non primary key columns in the table should depend DIRECTLY on the entire primary key.

http://dotnetanalysis.blogspot.com/2012/01/database-normalization-sql-server.html
```


### 数据仓库理论

https://www.cnblogs.com/muchen/p/5305658.html

#### 数据建模

https://www.cnblogs.com/muchen/p/5310732.html

* Kimball(纬度模型) vs Inmon(关系模型)

![Inmon model](./datawarehouse-theory_images/inmon_model.jpg)

上图为关系模型的建模方式，关系建模又叫ER建模，是数据仓库之父Inmon推崇的，其从全企业的高度设计一个3NF模型的方法，用实体加关系描述的数据模型描述企业业务架构，在范式理论上符合3NF，其是站在企业角度进行面向主题的抽象，而不是针对某个具体业务流程的，它更多是面向数据的整合和一致性治理，正如Inmon所希望达到的“single version of the truth”。

但是要采用此方法进行构建，也有其挑战：

* 需要全面了解企业业务和数据
* 实施周期非常长
* 对建模人员的能力要求也非常高

![Kimball model](./datawarehouse-theory_images/kimball.jpg)

上图为纬度模型的建模方式。维度模型则是数据仓库领域另一位大师Ralph Kimball 所倡导的。维度建模以分析决策的需求为出发点构建模型，一般有较好的大规模复杂查询的响应性能，更直接面向业务，典型的代表是我们比较熟知的星形模型，以及在一些特殊场景下适用的雪花模型。查看上图，可以发现，中间是一张事实表（存数据），周围围绕了多个纬度表（存纬度信息），这就是星型模型。

Inmon的ER建模优点体现在规范性较好，冗余小，数据集成和数据一致性方面得到重视，适用于较为大型的企业级、战略级的规划，但缺点是需要全面了解企业业务、数据和关系，对于建模人员要求很高，实施周期非常长，成本昂贵，笔者刚进公司的时候就经历了中国移动的的ER数据仓库项目，的确不是一个新人能短时消化的。 

Kimball的维度建模相对能快速上手，快速交付，但缺点是冗余会较多，灵活性比较差，但其实现在看来也没什么，淘宝在大数据之路书中也提到“淘宝数据平台变迁的过程正好解释了二者的不同，最初，淘宝业务单一、系统简单，主要是简单的报表系统；后期数据量越来越大，系统越来越多，尝试用ER建模的数据仓库，但是在实践中发现快速变化的业务之下，构建ER模型的风险和难度都很高，现在则主要采用基于维度建模的模型方法了。”



```
微软的BI主要是基于Kimball模型的, 这个模型是反数据库三范式的, 提出了雪花模型和星型模型, 区分了事实表和维度表. Kimball还提出了一致性维度的概念. 把不同数据源的维度统一更新到一个维度上去. 就是SSAS

Inmon用的比较少, 他的数仓是符合范式(3NF)的设计, 然后用于分析的数据集市从这个normalized的数仓中派生数据, 好处是数仓是normalized的, 数据的准确性很高, 没有什么冗余的数据, 但是维护和开发工作量巨大.
常说的面向主题的数据仓库，就是Inmon的模型。

维度建模的方式: 星型模型和雪花模型

星型模型和雪花模型是区别于传统关系型数据库的三范式建模的一种建模方式, 星型模型运用广泛,效率高, 而雪花模型运用较少, 但往往会作配角存在. 为什么有了星型模型还要有雪花模型呢? 一个典型的例子就是为了支持多对多关系. 维度表和事实表见有多对多的关系. 此外当一个维度的数量级大到一定程度时, 如果用雪花模型能减少冗余数据的时候,也可以尝试使用雪花模型.

```

另，参考：https://zhuanlan.zhihu.com/p/27426819


* 纬度模型(Kimball)：

核心概念：纬度表，事实表

模型：星形模型 vs 雪花模型

http://lxw1234.com/archives/2018/01/890.htm

https://www.infoq.cn/article/2017/10/Dimensional-Kimball-big-data-Had

http://www.databaseanswers.org/downloads/Dimensional_Modelling_by_Example.pdf

Kimball模型数据仓库建模技巧：https://zhuanlan.zhihu.com/p/26908834



结论：

```
（1）雪花模型在星形模型的基础上，将纬度表拆的更细。

```

* ODS/DW/DM


* 拉链表/全量表/流量表

举一个例子，一个支付系统，里面有账户余额表，交易流水表，订单表。有交易行为时，流程是先生成订单表，用户付款后，生成流水，修改用户账户余额（一般生成流水，修改账户余额要在一个事务中，此处不是重点，就不描述了）。

流水表对应数据仓库中的概念就是流量表

账户余额表对应的就是数据仓库中的全量表，是一个维护全量数据当前状态的表。

那么拉链表是什么，如果你把账户余额的最初的数据，还有每一次账户余额的变化的binlog 都保存到另一张表里面，这个表就是拉链表，我们内部一般叫它镜像表。这个表的特点是，能够查到任意账户在任意时刻的账户余额，相当于是历史可追溯的。这个表与账户余额表的不同之处在于，账户余额表只有每个账户最新的余额状态。

账户余额表的表结构可以如下：

|accountid|currentcoin|updatetime|lastserialno|
| --- | --- | --- | --- |
| ac_123 | 30 | 2019-04-13 20:32:00 | mkrijhj2hj3h3g3 |

拉链表的表结构与账户余额表完全相同。（还有一种不同的表结构，就是拉链表里面每条记录保存了变化前，变化后的所有字段）

在财务上需求中，经常需要计算指定时刻全量用户的的期初金额，期末金额，用拉链表计算就很方便了，一个SQL搞定，追溯历史很方便，大致如下:

```
# v1
select sum(coin_1) as coin_result from
(
    select sum(coin) as coin_1
    from account
    WHERE updatetime < cast(to_timestamp('${start_time}','yyyy-MM-dd') AS BIGINT) * 1000
    AND accounttype = 'YH'
    AND currency = '00'
    AND accounttarget = '0'
union all
    select sum(t2.precoin) as coin_1 from
    (select accountid, min(updatetime) as updatetime, min(preupdatetime) as preupdatetime
    from account_snapshot
    where time_day >= cast(to_timestamp('${start_time}','yyyy-MM-dd') AS BIGINT)
    AND accounttype = 'YH'
    AND currency = '00'
    AND accounttarget = '0'
    group by accountid) as t1
    join account_snapshot as t2
    on t1.accountid = t2.accountid and t1.updatetime = t2.updatetime and t1.preupdatetime = t2.preupdatetime
) as ttx

# v2
select sum(coin_1) as coin_result from
(
    select sum(coin) as coin_1
    from account
    WHERE updatetime < cast(to_timestamp('${start_time}','yyyy-MM-dd') AS BIGINT) * 1000
    AND accounttype = 'YH'
    AND currency = '00'
    AND accounttarget = '0'
union all
    -- 与 v1 的效果相同，并且免去了join
    select sum(precoin) from account_snapshot
    where preupdatetime < cast(to_timestamp('${start_time}','yyyy-MM-dd') AS BIGINT) * 1000
    AND time_day >= cast(to_timestamp('${start_time}','yyyy-MM-dd') AS BIGINT)
    AND accounttype = 'YH'
    AND currency = '00'
    AND accounttarget = '0'
) as ttx
```

https://www.jianshu.com/p/799252156379


---

参考：

https://www.vertabelo.com/blog/technical-articles/data-warehouse-modeling-star-schema-vs-snowflake-schema

https://www.computerweekly.com/tip/Inmon-or-Kimball-Which-approach-is-suitable-for-your-data-warehouse

https://blog.csdn.net/sinat_28472983/article/details/80948943
