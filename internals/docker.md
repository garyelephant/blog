## docker原理

*    How to limit resources using cgroups on centos 6

https://www.digitalocean.com/community/tutorials/how-to-limit-resources-using-cgroups-on-centos-6

*    Resource management in Docker

https://goldmann.pl/blog/2014/09/11/resource-management-in-docker/

*    Docker基础技术：Linux CGroup

http://coolshell.cn/articles/17049.html

*    Docker背后的内核知识——cgroups资源限制

http://www.infoq.com/cn/articles/docker-kernel-knowledge-cgroups-resource-isolation

*    CGroup 介绍、应用实例及原理描述

http://www.ibm.com/developerworks/cn/linux/1506_cgroup/index.html

*    Cgroups控制cpu，内存，io示例

http://www.cnblogs.com/yanghuahui/p/3751826.html

*    Red Hat Enterprise Linux 6 Resource Management Guide (Cgroups)

https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Resource_Management_Guide/index.html

*    Docker基础技术：Linux Namespace（上）

http://coolshell.cn/articles/17010.html

*    Docker基础技术：Linux Namespace（下）

http://coolshell.cn/articles/17029.html

*    Docker基础技术：AUFS

http://coolshell.cn/articles/17061.html

*    Docker基础技术：DeviceMapper

http://coolshell.cn/articles/17200.html

*    10张图带你深入理解Docker容器和镜像

http://dockone.io/article/783

---

### Docker 性能开销测试

*    Measuring Docker IO overhead

https://www.percona.com/blog/2016/02/11/measuring-docker-io-overhead/

*    Measuring Percona Server Docker CPU/network overhead

https://www.percona.com/blog/2016/02/05/measuring-docker-cpu-network-overhead/

*    An Updated Performance Comparison of Virtual Machines and Linux Containers

http://domino.research.ibm.com/library/cyberdig.nsf/papers/0929052195DD819C85257D2300681E7B/$File/rc25482.pdf

---

### Docker Network

*    Docker Networking 101 – The defaults

http://www.dasblinkenlichten.com/docker-networking-101/

*    Docker Networking 101 – Host mode

http://www.dasblinkenlichten.com/docker-networking-101-host-mode/

*    Docker Networking 101 – Mapped Container Mode

www.dasblinkenlichten.com/docker-networking-101-mapped-container/

*    Docker networking 101 – User defined networks

http://www.dasblinkenlichten.com/docker-networking-101-user-defined-networks/

*    Docker networks feature overview

https://docs.docker.com/engine/userguide/networking/

*    Docker Network configuration

https://docs.docker.com/v1.8/articles/networking/

*    Docker Networking: Reborn

http://container42.com/2015/10/30/docker-networking-reborn/

*    weave: Simple, resilient multi-host Docker networking

https://github.com/weaveworks/weave

*    Docker containers networking - Tutorial

http://www.dedoimedo.com/computers/docker-networking.html

*    A Brief Primer on Docker Networking Rules: EXPOSE, -p, -P, --link

https://www.ctl.io/developers/blog/post/docker-networking-rules/

---

Docker 中常见的 Runtime constraints on resources 可以参考：

https://docs.docker.com/engine/reference/run/

```
$ docker run --help | grep -C 5 "cpu"
--cpu-shares=0                  CPU shares (relative weight)
--cpu-period=0                  Limit CPU CFS (Completely Fair Scheduler) period
--cpu-quota=0                   Limit CPU CFS (Completely Fair Scheduler) quota
--cpuset-cpus=                  CPUs in which to allow execution (0-3, 0,1)
--cpuset-mems=                  MEMs in which to allow execution (0-3, 0,1)
```

```
$ docker run --help | grep -C 5 "memory"
--kernel-memory=                Kernel memory limit
-m, --memory=                   Memory limit
--memory-reservation=           Memory soft limit
--memory-swap=                  Total memory (memory + swap), '-1' to disable swap
--memory-swappiness=-1          Tuning container memory swappiness (0 to 100)
```
