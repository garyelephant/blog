### 1. Java 语言特性

#### 1.1 Exception 和 Error

1.1.1 Exception 和 Error 的关系

Exception 和 Error 都是继承了 Throwable 类，在 Java 中只有 Throwable 类型的实例才可以被抛出（throw）或者捕获（catch），它是异常处理机制的基本组成类型。

Exception 和 Error 体现了 Java 平台设计者对不同异常情况的分类。Exception 是程序正常运行中，可以预料的意外情况，可能并且应该被捕获，进行相应处理。

Error 是指在正常情况下，不大可能出现的情况，绝大部分的 Error 都会导致程序（比如 JVM 自身）处于非正常的、不可恢复状态。既然是非正常情况，所以不便于也不需要捕获，常见的比如OutOfMemoryError 之类，都是 Error 的子类。

1.1.2 Checked Exception / Unchecked Exception

Exception 又分为可检查（checked）异常和不检查（unchecked）异常，可检查异常在源代码里必须显式地进行捕获处理，这是编译期检查的一部分。前面我介绍的不可查的 Error，是Throwable 不是 Exception。

1.1.3 RuntimeException

1.1.4 Exception 处理最佳实践

下面的代码反映了异常处理中哪些不当之处？

```
try {
  // 业务代码
  // …
  Thread.sleep(1000L);
} catch (Exception e) {
  // Ignore it
}

```

这段代码虽然很短，但是已经违反了异常处理的两个基本原则。

第一，尽量不要捕获类似 Exception 这样的通用异常，而是应该捕获特定异常，在这里是 Thread.sleep() 抛出的 InterruptedException。

第二，不要生吞（swallow）异常。生吞异常，往往是基于假设这段代码可能不会发生，或者感觉忽略异常是无所谓的，但是千万不要在产品代码做这种假设！


#### 1.2 反射机制

对于 Java 语言的反射机制本身，如果你去看一下 java.lang 或 java.lang.reflect 包下的相关抽象，就会有一个很直观的印象了。Class、Field、Method、Constructor 等，这些完全就是我们去操作类和对象的元数据对应。反射各种典型用例的编程，相信有太多文章或书籍进行过详细的介绍，我就不再赘述了，至少你需要掌握基本场景编程，这里是官方提供的参考文档：https://docs.oracle.com/javase/tutorial/reflect/index.html

功能：
* 在运行时能判断任意一个对象所属的类。
* 在运行时能构造任意一个类的对象。
* 在运行时判断任意一个类所具有的成员变量和方法。
* 在运行时调用任意一个对象的方法。

说大白话就是，利用Java反射机制我们可以加载一个运行时才得知名称的class，获悉其构造方法，并生成其对象实体，能对其fields设值并唤起其methods。

应用场景：
反射技术常用在各类通用框架开发中。因为为了保证框架的通用性，需要根据配置文件加载不同的对象或类，并调用不同的方法，这个时候就会用到反射——运行时动态加载需要加载的对象。

关于反射，有一点我需要特意提一下，就是反射提供的 AccessibleObject.setAccessible (boolean flag)。它的子类也大都重写了这个方法，这里的所谓 accessible 可以理解成修饰成员的 public、protected、private，这意味着我们可以在运行时修改成员访问限制！

setAccessible 的应用场景非常普遍，遍布我们的日常开发、测试、依赖注入等各种框架中。比如，在 O/R Mapping 框架中，我们为一个 Java 实体对象，运行时自动生成 setter、getter 的逻辑，这是加载或者持久化数据非常必要的，框架通常可以利用反射做这个事情，而不需要开发者手动写类似的重复代码。



#### 1.3 动态代理

* 静态代理：事先写好代理类，可以手工编写，也可以用工具生成。缺点是每个业务类都要对应一个代理类，非常不灵活。

* 动态代理：运行时自动生成代理对象。缺点是生成代理代理对象和调用代理方法都要额外花费时间。
  
  * JDK动态代理：基于Java反射机制实现，必须要实现了接口的业务类才能用这种办法生成代理对象。新版本也开始结合ASM机制。
  
  * cglib动态代理：基于ASM机制实现，通过生成业务类的子类作为代理类。

为其他对象提供一种代理以控制对这个对象的访问。在某些情况下，一个对象不适合或者不能直接引用另一个对象，而代理对象可以在两者之间起到中介的作用（可类比房屋中介，房东委托中介销售房屋、签订合同等）。

所谓动态代理，就是实现阶段不用关心代理谁，而是在运行阶段才指定代理哪个一个对象（不确定性）。如果是自己写代理类的方式就是静态代理（确定性）。

组成要素：

(动态)代理模式主要涉及三个要素：
其一：抽象类接口

其二：被代理类（具体实现抽象接口的类）

其三：动态代理类：实际调用被代理类的方法和属性的类

实现方式:

实现动态代理的方式很多，比如 JDK 自身提供的动态代理，就是主要利用了反射机制。还有其他的实现方式，比如利用字节码操作机制，类似 ASM、CGLIB（基于 ASM）、Javassist 等。

举例，常可采用的JDK提供的动态代理接口InvocationHandler来实现动态代理类。其中invoke方法是该接口定义必须实现的，它完成对真实方法的调用。通过InvocationHandler接口，所有方法都由该Handler来进行处理，即所有被代理的方法都由InvocationHandler接管实际的处理任务。此外，我们常可以在invoke方法实现中增加自定义的逻辑实现，实现对被代理类的业务逻辑无侵入。

一个利用JDK自带动态代理机制的代码示例：

```
public class MyDynamicProxy {
    public static  void main (String[] args) {
        HelloImpl hello = new HelloImpl();
        MyInvocationHandler handler = new MyInvocationHandler(hello);
        // 构造代码实例
        Hello proxyHello = (Hello) Proxy.newProxyInstance(HelloImpl.class.getClassLoader(), HelloImpl.class.getInterfaces(), handler);
        // 调用代理方法
        proxyHello.sayHello();
    }
}
interface Hello {
    void sayHello();
}
class HelloImpl implements  Hello {
    @Override
    public void sayHello() {
        System.out.println("Hello World");
    }
}
 class MyInvocationHandler implements InvocationHandler {
    private Object target;
    public MyInvocationHandler(Object target) {
        this.target = target;
    }
    @Override
    public Object invoke(Object proxy, Method method, Object[] args)
            throws Throwable {
        System.out.println("Invoking sayHello"); // 这里插入了与业务逻辑无关的，由代理类实现的逻辑，比如：打印日志，权限校验等。
        Object result = method.invoke(target, args);
        return result;
    }
}


```


#### 1.4 常见语言特性

##### 1.4.1 Immutable vs Mutable Object 

immutable Objects就是那些一旦被创建，它们的状态就不能被改变的Objects，每次对他们的改变都是产生了新的immutable的对象，而mutable Objects就是那些创建后，状态可以被改变的Objects.

举个例子：String和StringBuilder，String是immutable的，每次对于String对象的修改都将产生一个新的String对象，而原来的对象保持不变，而StringBuilder是mutable，因为每次对于它的对象的修改都作用于该对象本身，并没有产生新的对象。

【Immutable objects 在并发环境下的应用】：

使用Immutable类的好处：

1）Immutable对象是线程安全的，可以不用被synchronize就在并发环境中共享

2）Immutable对象简化了程序开发，因为它无需使用额外的锁机制就可以在线程间共享

3）Immutable对象提高了程序的性能，因为它减少了synchroinzed的使用

4）Immutable对象是可以被重复使用的，你可以将它们缓存起来重复使用，就像字符串字面量和整型数字一样。你可以使用静态工厂方法来提供类似于valueOf（）这样的方法，它可以从缓存中返回一个已经存在的Immutable对象，而不是重新创建一个。

immutable也有一个缺点就是会制造大量垃圾，由于他们不能被重用而且对于它们的使用就是”用“然后”扔“，字符串就是一个典型的例子，它会创造很多的垃圾，给垃圾收集带来很大的麻烦。当然这只是个极端的例子，合理的使用immutable对象会创造很大的价值。

Java创建一个Immutable Object 的方法参考： 

https://my.oschina.net/jasonultimate/blog/166810

https://blog.csdn.net/qq_35691619/article/details/84699317

---

### 2. JVM

JVM 内存模型

【JVM 多线程内存模型】

Java 程序执行步骤

Java 类加载机制

类加载过程

自定义class loader

垃圾收集原理

常见的垃圾回收器, 如 SerialGC、Parallel GC、 CMS、 G1

参考： 《深入理解 Java 虚拟机》

---

### 3. Java 核心类库

#### 3.1 集合包 java.util

##### 3.1.1 Hashtable、 HashMap、 LinkedHashMap、 TreeMap 的功能特性和底层实现原理.(重点是HashMap)

Hashtable 用 synchronized 实现了全局锁，在并发场景下，效率较低。 因为它的实现基本就是将 put、get、size 等各种方法加上“synchronized”

HashMap 不具备并发处理能力，并发场景下可以用ConcurrentHashMap来代替。 

LinkedHashMap 是HashMap的子类实现，用双向链表实现了元素遍历顺序与插入顺序相同，对于需要。 【插入顺序】

TreeMap 则是基于红黑树的一种提供顺序访问的 Map，和 HashMap 不同，它的 get、put、remove 之类操作都是 O（log(n)）的时间复杂度，具体顺序可以由指定的 Comparator 来决定，或者根据键的自然顺序来判断

HashMap的实现原理:

（1）数组 + 链表的数据结构，使用hash的方式确定元素在数据中的位置，数组中的每个元素上面挂一个链表。

（2）元素的 hashcode(), equals() 方法的实现约定。  hashcode() 用于决定元素所处的数组位置； get()元素时， equals() 决定当 hash值相同时，应该获取链表上的哪个元素。

（3）HashMap 容量、负载因子

（4）链表转换成树

#### 3.2 并发包 java.util.concurrent

##### 3.2.1 并发容器 ConcurrentHashMap

如何保证集合是线程安全的? ConcurrentHashMap如何实现高效地线程安全？

![concurrentHashMap java1.7 数据结构](./java_images/ConcurrentHashMap-结构.png)

https://time.geekbang.org/column/article/8137

##### 3.2.2 并发容器 CopyOnWriteArrayList

##### 3.2.3 线程安全队列 （Queue/Deque），ArrayBlockingQueue，SynchronousQueue

#### 3.3 IO包, NIO


---

### 4. Java并发编程

#### 4.1 volatile, synchronized

在看一下volatile, Volatile修饰的成员变量在每次被线程访问时，都强迫从共享内存中重读该成员变量的值。而且，当成员变量发生变化时，强迫线程将变化值回写到共享内存。这样在任何时刻，两个不同的线程总是看到某个成员变量的值是相同的，更简单一点理解就是volatile修饰的变量值发生变化时对于另外的线程是可见的。

如何正确使用volatile可以参考下面这篇文章：

http://www.ibm.com/developerworks/cn/java/j-jtp06197.html Java 理论与实践: 正确使用 Volatile 变量

#### 4.2 Immutable Object

#### 4.3 Java Concurrent库

##### 4.3.1 ConcurrentHashMap, CopyOnWriteArrayList

##### 4.3.2 线程安全队列 （Queue/Deque），ArrayBlockingQueue，SynchronousQueue

##### 4.3.3 AtomicXXXX

##### 4.3.4 ThreadPool, ExecutorService

##### 4.3.5 Semaphore, CountdownLatch, ReentrantLock

#### 4.4 sun.misc.Unsafe API, CAS

Java无法直接访问底层操作系统，而是通过本地（native）方法来访问。不过尽管如此，JVM还是开了一个后门，JDK中有一个类Unsafe，它提供了硬件级别的原子操作 ---> 使用 Unsafe

##### 4.4.1 CAS

CAS 操作包含三个操作数 —— 内存位置（V）、预期原值（A）和新值(B)。如果内存位置的值与预期原值相匹配，那么处理器会自动将该位置值更新为新值。否则，处理器不做任何操作。无论哪种情况，它都会在 CAS 指令之前返回该位置的值。CAS 有效地说明了“我认为位置 V 应该包含值 A；如果包含该值，则将 B 放到这个位置；否则，不要更改该位置，只告诉我这个位置现在的值即可。” Java并发包(java.util.concurrent)中大量使用了CAS操作,涉及到并发的地方都调用了sun.misc.Unsafe类方法进行CAS操作。

##### 4.4.2 Unsafe 有什么用？ 有哪些API？ 怎么用？


http://www.cnblogs.com/mickole/articles/3757278.html

https://my.oschina.net/gordonfor/blog/1922683

下面来看看java中具体的CAS操作类sun.misc.Unsafe。Unsafe类提供了硬件级别的原子操作，Java无法直接访问到操作系统底层（如系统硬件等)，为此Java使用native方法来扩展Java程序的功能。具体实现使用c++,详见文件sun.misc.natUnsafe.cc();sun.misc包的源代码可以在这里找到：

http://www.oschina.net/code/explore/gcc-4.5.2/libjava/sun/misc

1、通过Unsafe类可以分配内存，可以释放内存；

类中提供的3个本地方法allocateMemory、reallocateMemory、freeMemory分别用于分配内存，扩充内存和释放内存，与C语言中的3个方法对应。

```
public native long allocateMemory(long l);
public native long reallocateMemory(long l, long l1);
public native void freeMemory(long l);
```

2、可以定位对象某字段的内存位置，也可以修改对象的字段值，即使它是私有的；

字段的定位：

JAVA中对象的字段的定位可能通过staticFieldOffset方法实现，该方法返回给定field的内存地址偏移量，这个值对于给定的filed是唯一的且是固定不变的。

getIntVolatile方法获取对象中offset偏移地址对应的整型field的值,支持volatile load语义。

getLong方法获取对象中offset偏移地址对应的long型field的值

数组元素定位：

Unsafe类中有很多以BASE_OFFSET结尾的常量，比如ARRAY_INT_BASE_OFFSET，ARRAY_BYTE_BASE_OFFSET等，这些常量值是通过arrayBaseOffset方法得到的。arrayBaseOffset方法是一个本地方法，可以获取数组第一个元素的偏移地址。Unsafe类中还有很多以INDEX_SCALE结尾的常量，比如 ARRAY_INT_INDEX_SCALE ， ARRAY_BYTE_INDEX_SCALE等，这些常量值是通过arrayIndexScale方法得到的。arrayIndexScale方法也是一个本地方法，可以获取数组的转换因子，也就是数组中元素的增量地址。将arrayBaseOffset与arrayIndexScale配合使用，可以定位数组中每个元素在内存中的位置。

3、挂起与恢复

将一个线程进行挂起是通过park方法实现的，调用 park后，线程将一直阻塞直到超时或者中断等条件出现。unpark可以终止一个挂起的线程，使其恢复正常。整个并发框架中对线程的挂起操作被封装在 LockSupport类中，LockSupport类中有各种版本pack方法，但最终都调用了Unsafe.park()方法。

4、CAS操作

是通过compareAndSwapXXX方法实现的

```
/**
* 比较obj的offset处内存位置中的值和期望的值，如果相同则更新。此更新是不可中断的。
* 
* @param obj 需要更新的对象
* @param offset obj中整型field的偏移量
* @param expect 希望field中存在的值
* @param update 如果期望值expect与field的当前值相同，设置filed的值为这个新值
* @return 如果field的值被更改返回true
*/
public native boolean compareAndSwapInt(Object obj, long offset, int expect, int update);
```

CAS操作有3个操作数，内存值M，预期值E，新值U，如果M==E，则将内存值修改为B，否则啥都不做。


##### 4.4.3 AtomicInteger 实现原理

https://www.cnblogs.com/xrq730/p/4976007.html

#### 4.5 java.io 同步IO / java.nio 异步IO

TODO: 

https://time.geekbang.org/column/article/8369

https://time.geekbang.org/column/article/8393

---

### 5. Java内置工具



---

### FAQ 1:

Q1: java程序执行步骤 ?

首先javac编译器将源代码编译成字节码。

然后jvm类加载器加载字节码文件，然后通过解释器逐行解释执行，这种方式的执行速度相对会比较慢。有些方法和代码块是高频率调用的，也就是所谓的热点代码，所以引进JIT技术，提前将这类字节码直接编译成本地机器码。这样类似于缓存技术，运行时再遇到这类代码直接可以执行，而不是先解释后执行。


Q2: 请对比 Exception 和 Error，另外，运行时异常与一般异常有什么区别？



Q3: NoClassDefFoundError vs ClassNOtFoundException ?
NoClassDefFoundError 是一个错误(Error，而 ClassNOtFoundException 是一个异常，在Java中对于错误和异常的处理是不同的，我们可以从异常中恢复程序但却不应该尝试从错误中恢复程序。

Q4: Java 反射机制，动态代理是基于什么原理？

考点：

* 考察你对反射机制的了解和掌握程度。

* 动态代理解决了什么问题，在你业务系统中的应用场景是什么？

* JDK 动态代理在设计和实现上与 ASM、cglib（基于 ASM）、Javassist 方式有什么不同，进而如何取舍？


Q4: Hashtable、 HashMap、 TreeMap 有什么不同？

三者均实现了Map接口，存储的内容是基于key-value的键值对映射，一个映射不能有重复的键，一个键最多只能映射一个值。

（1）元素特性
HashTable中的key、value都不能为null；HashMap中的key、value可以为null，很显然只能有一个key为null的键值对，但是允许有多个值为null的键值对；TreeMap中当未实现 Comparator 接口时，key 不可以为null；当实现 Comparator 接口时，若未对null情况进行判断，则key不可以为null，反之亦然。

（2）顺序特性
HashTable、HashMap具有无序特性。TreeMap是利用红黑树来实现的（树中的每个节点的值，都会大于或等于它的左子树种的所有节点的值，并且小于或等于它的右子树中的所有节点的值），实现了SortMap接口，能够对保存的记录根据键进行排序。所以一般需要排序的情况下是选择TreeMap来进行，默认为升序排序方式（深度优先搜索），可自定义实现Comparator接口实现排序方式。

（3）初始化与增长方式
初始化时：HashTable在不指定容量的情况下的默认容量为11，且不要求底层数组的容量一定要为2的整数次幂；HashMap默认容量为16，且要求容量一定为2的整数次幂。
扩容时：Hashtable将容量变为原来的2倍加1；HashMap扩容将容量变为原来的2倍。

（4）线程安全性
HashTable其方法函数都是同步的（采用synchronized修饰），不会出现两个线程同时对数据进行操作的情况，因此保证了线程安全性。也正因为如此，在多线程运行环境下效率表现非常低下。因为当一个线程访问HashTable的同步方法时，其他线程也访问同步方法就会进入阻塞状态。比如当一个线程在添加数据时候，另外一个线程即使执行获取其他数据的操作也必须被阻塞，大大降低了程序的运行效率，在新版本中已被废弃，不推荐使用。
HashMap不支持线程的同步，即任一时刻可以有多个线程同时写HashMap;可能会导致数据的不一致。如果需要同步
（1）可以用 Collections的synchronizedMap方法；
（2）使用ConcurrentHashMap类，相较于HashTable锁住的是对象整体， ConcurrentHashMap基于lock实现锁分段技术。首先将Map存放的数据分成一段一段的存储方式，然后给每一段数据分配一把锁，当一个线程占用锁访问其中一个段的数据时，其他段的数据也能被其他线程访问。ConcurrentHashMap不仅保证了多线程运行环境下的数据访问安全性，而且性能上有长足的提升。

（5）一段话 HashMap
HashMap基于哈希思想，实现对数据的读写。当我们将键值对传递给put()方法时，它调用键对象的hashCode()方法来计算hashcode，让后找到bucket位置来储存值对象。当获取对象时，通过键对象的equals()方法找到正确的键值对，然后返回值对象。HashMap使用链表来解决碰撞问题，当发生碰撞了，对象将会储存在链表的下一个节点中。 HashMap在每个链表节点中储存键值对对象。当两个不同的键对象的hashcode相同时，它们会储存在同一个bucket位置的链表中，可通过键对象的equals()方法用来找到键值对。如果链表大小超过阈值（TREEIFY_THRESHOLD, 8），链表就会被改造为树形结构。

---

### References:

1. 极客时间 "Java核心技术36讲" https://time.geekbang.org
2. 《深入理解 Java 虚拟机》


