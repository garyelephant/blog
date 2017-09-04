# 数据结构与算法

## 排序算法

8大排序算法的实现，复杂度，稳定性。

![sort-overview](./data-structure-algorithms_images/sort-overview.jpg)

## 查找算法

顺序查找，二分查找，分块查找，散列表，利用树形结构实现查找（二分查找树，红黑树，BTree）

## 跳跃表（SkipList）

什么是跳跃表？https://weibo.com/ttarticle/p/show?id=2309404129356560600034

![skip list 1](./data-structure-algorithms_images/skiplist.png)

跳表具有如下性质：

(1) 由很多层结构组成

(2) 每一层都是一个有序的链表

(3) 最底层(Level 1)的链表包含所有元素

(4) 如果一个元素出现在 Level i 的链表中，则它在 Level i 之下的链表也都会出现。

(5) 每个节点包含两个指针，一个指向同一链表中的下一个元素，一个指向下面一层的元素。

跳跃表的查找：

![skip list search](./data-structure-algorithms_images/search_path_on_skiplist.png)

```
/* 如果存在 x, 返回 x 所在的节点， 
 * 否则返回 x 的后继节点 */  
find(x)   
{  
    p = top;  
    while (1) {  
        while (p->next->key < x)  
            p = p->next;  
        if (p->down == NULL)   
            return p->next;  
        p = p->down;  
    }  
}  
```

跳跃表的插入:

先确定该元素要占据的层数 K（采用丢硬币的方式，这完全是随机的）
然后在 Level 1 ... Level K 各个层的链表都插入元素。

![skip list search](./data-structure-algorithms_images/skiplist_insertions.png)

跳跃表删除节点：

无论是插入，还是删除，都是先查找。删除节点的过程就是普通链表删除节点的过程。

skiplist的插入，删除、查找时间复杂度：O(logN):

SkipList是一种概率算法，非常依赖于生成的随机数。这里不能用rand() % MAX_LEVEL的简单做法，而要用满足p=1/2几何分布的随机数。

来看RandomLevel()的代码：

```
int SkipList::RandomLevel(void) {
    int level = 0;
    while(rand() % 2 && level < MAX_LEVEL - 1)
        ++level;
    return level;
}
```

这里不做太多的数学分析，只做直观解释。考虑MAX_LEVEL = 4的情形，可能的返回值为0、1、2、3，显然出现概率分别为：

P(0) = (1/2)^0 * (1/2) = 1/2
P(1) = (1/2)^1 * (1/2) = 1/4
P(2) = (1/2)^2 * (1/2) = 1/8
P(3) = 1 - P(0) - P(1) - P(2) = 1/8

假设有16个元素的话，可以预计第0层有16个元素，第1层约有16 - 8 = 8个元素，第2层约有16 - 8 - 4 = 4个元素，第3层约有16 - 8 -4 -2 = 2个元素，从底向上每层元素数量大约减少一半。

SkipList层数合适时自顶向下搜索，理想情况下每下降一层，搜索范围减小一半，达到类似二分查找的效果，效率为O(lgn)；最坏情况下也只是curr从head移动到tail，效率为O(n)。


http://kenby.iteye.com/blog/1187303

http://zhangtielei.com/posts/blog-redis-skiplist.html

FAQ:

Q1: skiplist 有几层是如何决定的？某个节点在哪一层出现是如何决定的？

A1: 插入的新节点，都会通过`投硬币`觉得其所在的最大层数；所有节点所在最大层数的最大值，即跳跃表的层数。

Q2: 跳跃表查找的起始点在哪里？

A2: 最左侧最上层的节点（有点类似二分查找树）。

Q3: Java中的相关实现？

A3: ConcurrentSkipListMap, ConcurrentSkipListSet

Q4: 跳跃表 vs 平衡树(AVL, 红黑树, 2-3树) ? 

A4: 跳表是一种随机性的数据结构，相对于平衡树来说，跳表更加的简单，能一口气实现红黑树,AVL这样的平衡树的人，还是太少了，而且内部确实复杂，调试, 用起来太麻烦。 
同样跳表还可以做到平衡树那样的查找时间，特别是在并发的场景下面，由于红黑树的插入或者删除会做rebalance这样操作，那么影响的数据就会变多，锁的粒度就变大。
但是跳表的插入或者删除操作影响的数据会很小，锁的粒度就会小，这样在大数据量的情况下，跳表的性能自然就会比红黑树要好。

https://softwareengineering.stackexchange.com/questions/287254/how-does-a-skip-list-work

Q5: 跳跃表的生产环境应用？

A5: Redis SortedSet, Lucene

Q6: 跳跃表的Java实现？


## 树的数据结构与常用算法（重点红黑树、B-Tree）

### 树的遍历：前序，中序，后序

### 二叉查找树和查找算法

### B-树和B+树

> B-树就是B树，中间的横线不是减号

B-树是一种多路平衡查找树，它的每个节点最多包含m个孩子，m被称为B树的阶。m的大小取决于磁盘页的大小。

一个m阶的B-树具有如下几个特征：

```
1.根结点至少有两个子女。

2.每个中间节点都包含k-1个元素和k个孩子，其中 m/2 <= k <= m

3.每一个叶子节点都包含k-1个元素，其中 m/2 <= k <= m

4.所有的叶子结点都位于同一层。

5.每个节点中的元素从小到大排列，节点当中k-1个元素正好是k个孩子包含的元素的值域分划。
```

一个m阶的B+树具有如下几个特征：

```
1.有k个子树的中间节点包含有k个元素（B树中是k-1个元素），每个元素不保存数据，只用来索引，所有数据都保存在叶子节点。

2.所有的叶子结点中包含了全部元素的信息，及指向含这些元素记录的指针，且叶子结点本身依关键字的大小自小而大顺序链接。

3.所有的中间节点元素都同时存在于子节点，在子节点元素中是最大（或最小）元素。

```

![b+tree](./data-structure-algorithms_images/b+tree1.png)

B+树的优势：

```

1.单一节点存储更多的元素，使得查询的IO次数更少。

2.所有查询都要查找到叶子节点，查询性能稳定。

3.所有叶子节点形成有序链表，便于范围查询。

```



FAQ：

Q1: B+树的实现细节是什么样的？

Q2: B-树和B+树有什么区别？

Q3: MySQL 联合索引在B+树中如何存储？

Q4: 已经有了二叉查找树，为什么还需要B-/B+树？

Q5: B-/B+树？为什么适合做数据库，文件系统的索引结构？

Q6: B-/B+树？如何实现插入，查找，删除？

Q7: B-/B+树的Java 实现？


### 红黑树


## 哈希表：HashMap, LinkedHashMap

## 大数据算法

## 图的数据结构与常用算法


## References

http://blog.csdn.net/hguisu/article/details/7776068
http://www.runoob.com/w3cnote/sort-algorithm-summary.html

http://blog.csdn.net/hguisu/article/details/7776091
http://www.cnblogs.com/maybe2030/p/4715035.html

MySQL索引背后的数据结构及算法原理: http://blog.codinglabs.org/articles/theory-of-mysql-index.html

算法的可视化：https://www.cs.usfca.edu/~galles/visualization/Algorithms.html

B-树介绍：http://blog.jobbole.com/111757/

B+树介绍：https://news.uc.cn/a_1850348189949560112/