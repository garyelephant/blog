# Kafka关键技术点

### Kafka 快的原因

* 数据分片

* 端到端的数据压缩，减少了网络IO

producer端发送数据前，使用snappy进行压缩。consumer消费数据后，使用snappy解压。

* 顺序写入磁盘

* zero-copy

java nio 调用了linux系统底层的`sendfile()` 系统调用，文件读取到内核态的read buffer后，不再复制到用户态的application buffer，而是直接给socket buffer，然后发送给consumer，减少了2次IO(read buffer -> app buffer, app buffer -> socket buffer)和用户态内核态切换，效率提升200%以上。

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

* 文件系统缓存(mmap)，利用操作系统将文件直接映射到内存中，通过缺页访问来访问文件

> `mmap()`系统调用，mmap()函数将文件直接映射到用户程序的内存中，映射成功时返回指向目标区域的指针。这段内存空间可以用作进程间的共享内存空间，内核也可以直接操作这段空间。在映射文件之后，暂时不会拷贝任何数据到内存中，只有当访问这段内存时，发现没有数据，于是产生缺页访问，使用DMA操作将数据拷贝到这段空间中。可以直接将这段空间的数据拷贝到socket buffer中。所以也算是零复制技术。

同时，KAFKA采用了MMAP(Memory Mapped Files，内存映射文件)技术。很多现代操作系统都大量使用主存做磁盘缓存，一个现代操作系统可以将内存中的所有剩余空间用作磁盘缓存，而当内存回收的时候几乎没有性能损失。

由于KAFKA是基于JVM的，并且任何与Java内存使用打过交道的人都知道两件事：
▪ 对象的内存开销非常高，通常是实际要存储数据大小的两倍；
▪ 随着数据的增加，java的垃圾收集也会越来越频繁并且缓慢。

基于此，使用文件系统，同时依赖页面缓存就比使用其他数据结构和维护内存缓存更有吸引力：
▪ 不使用进程内缓存，就腾出了内存空间，可以用来存放页面缓存的空间几乎可以翻倍。
▪ 如果KAFKA重启，进行内缓存就会丢失，但是使用操作系统的页面缓存依然可以继续使用。

可能有人会问KAFKA如此频繁利用页面缓存，如果内存大小不够了怎么办？
KAFKA会将数据写入到持久化日志中而不是刷新到磁盘。实际上它只是转移到了内核的页面缓存。

利用文件系统并且依靠页缓存比维护一个内存缓存或者其他结构要好，它可以直接利用操作系统的页缓存来实现文件到物理内存的直接映射。完成映射之后对物理内存的操作在适当时候会被同步到硬盘上。

* NIO

---

## TODO

https://www.jianshu.com/p/d47de3d6d8ac

https://www.iteblog.com/archives/2227.html?from=related

https://www.iteblog.com/archives/2209.html?from=related

https://www.iteblog.com/archives/2215.html?from=related

https://www.iteblog.com/archives/2219.html?from=related

https://www.iteblog.com/archives/2232.html?from=related

https://www.iteblog.com/archives/2235.html?from=related
