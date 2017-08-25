# Parquet vs Carbondata vs Lucene vs Arrow vs mmdb

---

## 列示存储的优势：
1. 减少IO：只获取需要的列
2. 减少存储：列级别的压缩
3. 只读取需要的列，支持向量运算，能够获取更好的扫描性能。

---

Q&A:
1. parquet 如何存储嵌套结构？
2. parquet 中每个row group中所有row的顺序是如何决定的？
3. parquet 用到的 Nested record shredding/assembly • Algorithm borrowed from Google Dremel's column IO 是啥？
4. parquet Repetition levels, Definition levels和values是什么？

---

References:

https://github.com/apache/parquet-format
https://www.slideshare.net/julienledem/parquet-hadoop-summit-2013
https://research.google.com/pubs/pub36632.html
http://www.infoq.com/cn/articles/in-depth-analysis-of-parquet-column-storage-format
https://blog.twitter.com/engineering/en_us/a/2013/dremel-made-simple-with-parquet.html
https://github.com/apache/carbondata
http://carbondata.apache.org/
https://github.com/QiangCai/carbondata_guide
https://github.com/zzboy/lucene
https://github.com/apache/arrow
https://www.quora.com/How-will-Googles-Dremel-change-future-Hadoop-releases
