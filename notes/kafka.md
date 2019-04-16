# Kafka关键技术点

### Kafka 快的原因

* 数据分片

* 顺序写入磁盘

* NIO

* zero-copy

java nio 调用了linux系统底层的`sendfile()` 系统调用，文件读取到内核态的read buffer后，不再复制到用户态的application buffer，而是直接给socket buffer，然后发送给consumer，减少了2次IO(read buffer -> app buffer, app buffer -> socket buffer)和用户态内核态切换，效率提升200%以上。

类似的还有`mmap()`系统调用，mmap()函数将文件直接映射到用户程序的内存中，映射成功时返回指向目标区域的指针。这段内存空间可以用作进程间的共享内存空间，内核也可以直接操作这段空间。在映射文件之后，暂时不会拷贝任何数据到内存中，只有当访问这段内存时，发现没有数据，于是产生缺页访问，使用DMA操作将数据拷贝到这段空间中。可以直接将这段空间的数据拷贝到socket buffer中。所以也算是零复制技术。

类似的还有`copy-on-write` 技术，使用copy-on-write技术，使得在fork子进程时不复制内存页，而是共享内存页(也就是说，子进程也指向父进程的物理空间)，只有在该子进程需要修改某一块数据，才会将这一块数据拷贝到自己的app buffer中并进行修改，那么这一块数据就属于该子进程的私有数据，可随意访问、修改、复制。这在一定程度上实现了零复制，即使复制了一些数据块，也是在逐渐需要的过程进行复制的。

``` 
java.nio.FileChannel.transferTo(
    long position, 
    long count,                                
    WritableByteChannel target)
```

https://www.jianshu.com/p/694443d87600

https://www.jianshu.com/p/e76e3580e356

https://www.cnblogs.com/f-ck-need-u/p/7615914.html

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
