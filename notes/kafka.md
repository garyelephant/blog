# Kafka关键技术点

### Kafka 快的原因

* 数据分片

* 顺序写入磁盘

* NIO

* zero-copy

java nio 调用了linux系统底层的sendfile system call，文件读取到内核态的read buffer后，不再复制到用户态的application buffer，而是直接给socket buffer，然后发送给consumer，减少了2次IO(read buffer -> app buffer, app buffer -> socket buffer)和用户态内核态切换，效率提升200%以上。

``` 
java.nio.FileChannel.transferTo(
    long position, 
    long count,                                
    WritableByteChannel target)
```

https://www.jianshu.com/p/694443d87600

* 文件系统缓存

---

## TODO

https://www.jianshu.com/p/d47de3d6d8ac

https://www.iteblog.com/archives/2227.html?from=related

https://www.iteblog.com/archives/2209.html?from=related

https://www.iteblog.com/archives/2215.html?from=related

https://www.iteblog.com/archives/2219.html?from=related

https://www.iteblog.com/archives/2232.html?from=related

https://www.iteblog.com/archives/2235.html?from=related
