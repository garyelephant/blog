# Scala 关键技术点


## 基础数据结构用法

Seq, List, Vector

Tuple : https://alvinalexander.com/scala/scala-tuple-examples-syntax

## Scala 编程最佳实践

1. 优先采用面向表达式编程

面向表达式编程是个术语，意思是在代码中使用表达式而不用语句。表达式是可以求值的东西，语句是可以执行的东西，但是不返回值。举例：

```
def showError(errorCode: Int) : String = errorCode match {
  case 1 => "Network Failure"
  case 2 => "I/O Failure"
  case _ => "Unknown Error"
}
```

2. 优先选择不变性

不变性指对象一旦创建后就不再改变状态。这是函数式变成的基石之一，也是JVM上的面向对象编程的推荐实践之一。

3. 用 None不用null

Scala里，你可以用Option的None子类来代表这个意思，反过来用Option的Some子类代表一个初始化了的变量。

为什么不用null？

Option的最重要特性是可以被当作集合开袋。这意味着你可以对Option使用标准的map, flatmap, foreach等方法，
还可以用在for表达式里。这不仅有助于确保优美简洁的语法，而且开启了另一种不同的处理未初始化值的方法。

4. 函数式编程

5. 隐式转换

6. public 接口应当明确声明返回类型。

public 接口应当明确声明返回类型，避免泄漏实现细节。这样做还能稍稍加快编译速度，
因为编译器不需要去推断返回类型了，而且还让你的隐式转换有机会插一脚来把类型强制转换为你想要的类型。


---

## FAQ

1. Scala vs Java ?

2. `class` vs `object` vs `abstract class` vs `trait` vs `case class` ?

https://stackoverflow.com/questions/1755345/difference-between-object-and-class-in-scala

https://stackoverflow.com/questions/29207230/class-object-trait-sealed-trait-in-scala?rq=1

https://stackoverflow.com/questions/43171730/when-to-use-classes-vs-objects-vs-case-classes-vs-traits

trait 类似java的interface，当trait中提供了默认实现时，又类似java的abstract class。其实scala中也有abstract class

https://alvinalexander.com/scala/scala-trait-examples

https://stackoverflow.com/questions/1991042/what-is-the-advantage-of-using-abstract-classes-instead-of-traits?rq=1


3. scala java interop的注意事项？

https://alvinalexander.com/scala/how-to-wrap-scala-traits-used-accessed-java-classes-methods

https://stackoverflow.com/questions/7637752/using-scala-traits-with-implemented-methods-in-java

http://blog.muhuk.com/2016/06/04/how_to_call_scala_from_java_inheritance_singletons.html#.WcUgYdMjGRs

https://www.artima.com/pins1ed/combining-scala-and-java.html

4. List vs Seq vs Array vs Vector?

https://stackoverflow.com/questions/10866639/difference-between-a-seq-and-a-list-in-scala

---

## References

《快学Scala》

《Scala Cookbook》

《深入理解Scala》