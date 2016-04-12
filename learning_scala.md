# Cheatsheet of Learning Scala

## Why Scala ？

*	为并发而生？
*	基于JVM
*	比Java好？

## Notes

*	看不懂就做题

## Scala 解释器用法

```
# 代码段模式
> : paste

# 编译scala源文件
$ scalac test.scala
```

## 基础

注释：//

变量声明：val / var

类型声明：val gretting: String = null

类型转化："99.44".toDouble()

import: import.scala.math._  // 类似*

方法调用：不带参数的Scala方法通常不使用圆括号 "Hello".distinct

Scala对Java中的基本数据类型做了扩展，丰富了其操作能力，如基于String做了StringOps

伴生对象，apply方法：

lazy 声明的变量将在第一次被访问时才被初始化
```
lazy val words = scala.io.Source.fromFile("/u sr/share/dict/words").mkString
```

可以在函数中定义函数，在类中定义类。

## 控制结构

在scala中，表达式有值也有类型。

for循环的表达方式：

```
for (i <- 1 to 10)
	print(i)

# scala 中的for循环还有更多高级功能：生成器，守卫，变量定义
```

scala中没有提供break, continue语句来退出循环。

{}的最后一个表达式就是{}的值。

Uint类型相当于空，它只有一个值`()`

异常:
```
# throw表达式有特殊的类型Nothing, 在if/else中很有用。
if (x >= 0) { sqrt(x)
} else throw new IllegalArgumentException("x should not be negative")
# 第一个分支类型是Double, 第二个分支类型是Nothing。因此，if/else表达式的类型是Double。

# 捕获异常的语法是模式匹配语法：
try {
	process(new URL("http://www.example.com"))
} catch {
	case _: MalformedURLException => println("Bad URL")
	case ex: IOException => ex.printStackTrace()
} finally {
	// do some final thing
}
```


## 函数

函数定义：
```
# 非递归函数不需要指定返回类型
def abs(x: Double) = if (x >= 0) x else -x

# 如果函数体需要多个表达式完成，可以用代码块，块中最后一个表达式的值就是函数返回值。
def fac(n: Int) = {
	var r = 1
	for (i <- 1 to n) r = r * i
	r
}

# 递归函数
def fac(n: Int) Int = if ( n <= 0) 1 else n * fac(n - 1)

# 默认参数
def decorate(str: String, left: String = "[", right: String = "]") = left + str + right

# 变长参数
def sum(args: Int*) = {
	var result = 0
	for (arg <- args) result += arg
	result
}

# 过程: 不返回值的函数

def func(s: String): Unit = {
	......
}
```


## 数组相关操作

*	若长度固定则使用Array, 若长度可能变化则使用ArrayBuffer

```
# 所有元素初始化为0
val nums = new Array[Int](10)

# 已提供初始值时不要使用new
val s = Array("Hello", "World")
# 用()来访问元素
s(0) = "Goodbye"

# ArrayBuffer
import scala.collection.mutable.ArrayBuffer
val b = ArrayBuffer[Int]()
```

*	用for(elem <- arr)来遍历元素
*	用for(elem <- arr if ...) ... yield ... 来将数组转型为新数组
*	Array 常用方法:sum,max,min, sorted
*	Scala数组和Java数组可以互操作

多维数组

```
val matrix = Array.ofDim[Double](3, 4) // 3 x 4
```

## 映射(kv store)和元组

```
# 构造不可变映射
val scores = Map("Alice" -> 10, "Bob" -> 3, "Cindy" -> 8)
# 可变映射
val scores = scala.collection.mutable.Map("Alice" -> 10, "Bob" -> 3, "Cindy" -> 8)
# 空映射
val scores = new scala.collection.mutable.HashMap(String, Int)

```

## 类

```
class Counter {
	private var value = 0
	def increment() { value += 1 } // public by default
	def current() = value
	// 也可以这么写
	// def current = value
}

val myCounter = new Counter // 或new Counter()
// 一般改值器使用()，取值器去掉()
myCounter.increment()
println(myCounter.current)
```

类构造器：
*	主构造器, 与类定义交织在一起
*	辅助构造器，以def this(...)的方式定义


## 对象

用对象作为单例或存放工具方法

```
// Scala 没有静态方法或静态字段，可用object这个语法结构来达到同样目
的。
object Accounts {
	private var lastNumber = 0
	def newUniqueNumber() = { lastNumber += 1; lastNumber }
}
// 调用方法
Accounts.newUniqueNumber()
```

对象本质上拥有类的所有特性，只有一个例外：不能提供构造器参数。对于任何在Java中会使用单例对象的地方，在scala中都可以用对象来实现：
*	作为存放工具函数或常量的地方。
*	高效地共享单个不可变实例。
*	需要单例模式时。


类可以拥有一个同名的伴生对象

```
class Account {
	val id = Account.newUniqueNumber()
	private var balance = 0.0
	def deposit(amount: Double) { balance += amount }
	...
}

object Account { // 伴生对象
	private var lastNumber = 0
	private def newUniqueNumber() = { lastNumber += 1; lastNumber }
}
```


对象的apply方法通常用来构造伴生类的新实例：

```
// 当遇到如下形式的表达式时，apply方法就会被调用：
Object(arg1, ..., argN)
// 这样一个apply方法返回的是伴生类的对象
// 如Array对象定义了apply方法，让我们可以用下面这样的表达式创建数组：
Array("Marry", "had", "a", "little", "lamb")
// Array(100) vs new Array(100) ?
// Array(100)调用的是apply(100),输出一个只有一个元素的Array[Int],而new Array(100) 调用的是构造器this(100),结果是Array[Nothing], 包含了100个null元素。
```

定义apply方法的示例：
```
class Account private (val id: Int, initialBalance: Double) {
	private var balance = initialBalance
	...
}

object Account {
	def apply(initialBalance: Double) = new Account(newUniqueNumber(), initialBalance)
	...
}

# 这样就可以用如下代码来构造账号:

val acct = Account(1000.0)
```

## 包和引入

*	包也可以像内部类那样嵌套
*	包路径不是绝对路径
*	包声明链x.y.z并不自动将中间包x和x.y变成可见
*	位于文件顶部不带花括号的包声明在整个文件范围内有效
*	包对象可以持有函数和变量
*	引入语句可以引入包、类和对象
*	引入语句可以出现在任何位置
*	引入语句可以重命名和隐藏特定成员
*	java.lang , scala 和 Predef 总是被引入

创建包

```
package com {
	package horstmann {
		package impatient {
			class Employee
			...
		}
	}
}
# Employee可以在任意位置以com.horstmann.impatient.Employee访问到
```

作用域规则：可以访问上层作用域中的名称，包名是相对的。

串联式包语句：
```
package com.horstmann.impatient {
	// com和com.horstmann的成员在这里不可见
	package people {
		class Person
		...
	}
}
```

文件顶部标记法:
```
package com.horstmann.impatient
package people

class Person
...

# 等同于

package com.horstmann.impatient {
	package people {
		class Person
		...
	}
}
```

包对象：
```
包对象可以实现把工具函数或常量添加到包而不是某个Utils对象
package com.horstmann.impatient

package object people {
	val defaultName = "ABC"
}

package people {
	class Person {
		var name = defaultName // 从包对象拿到常量
	}
	...
}
```

引入:
```
// 任何地方都可以声明引入

// 可以在代码中直接写Color
import java.awt.Color

// 引入所有成员
import java.awt.Color._

// 想要包中的几个成员
import java.awt.{Color, Font}

// 重命名
import java.util.{HashMap => JavaHashMap}
import scala.collection.mutable._
```

隐式引入：
```
每个Scala程序都隐式引入如下：
import java.lang._
// 对于scala开头的包，完全不需要写这个前缀
import scala._
import Predef._
```

## 继承(代码复用的方式)

*	extends, final关键字与java相同
*	重写方法时必须用override
*	只有主构造器可以调用超类的主构造器
*	可以重写字段

```
// 扩展类
class Employee extends Person {
	var salary = 0.0
}

// 重写方法，重写非抽象方法必须使用override修饰符
public class Person {
	...
	override def toString = getClass.getName + "[name=" + name + "]"
}

// 调用超类方法使用super关键字
public class Employee extends Person {
	...
	override def toString = super.toString + "[salary=" + "]"
}

// 类型检查和转换
if (p.isInstanceOf[Employee]) {
	val s = p.asInstanceOf[Employee] //s的类型为Employee
}

// 如果想要测试p指向的是一个Employee对象但又不是其子类的话，可以用：
if (p.getClass == classOf[Employee])

// 子类的辅助构造器最终都会调用主构造器，只有主构造器可以调用超类的构造器。调用超类构造器的方式也同样交织在一起。
class Employee(name: String, age: Int, val salary: Double) extends Person(name, age)

// 重写字段的规则比较复杂，涉及def, val, var的应用

// 匿名子类, 可以通过包含带有定义或重写的代码块方式创建一个匿名的子类
var alien = new Person("Fred") {
	def greeting = "Greetings, Earthling! My name is Fred."
}

// 抽象类, 用abstract标记不能被实例化的类
abstract class Person(val name:String) {
	def id: Int // 没有方法体---这是一个抽象方法
}

// 在子类中重写超类的抽象方法时，不需要用override
class Employee(name: String) extends Person(name) {
	def id = name.hashCode // 不需要用override
}

// 抽象字段，没有初始值的字段
abstract class Person {
	val id: Int
	var name: String
}
```


## 文件和正则表达式

*	Source.fromFile(...).getLines.toArray 输出文件的所有行
*	Source.fromFile(...).mkString以字符串形式输出文件内容
*	将字符串转换为数字，可以用toInt或toDouble方法
*	使用Java的PrintWriter来写入文本文件
*	“abc”.r是一个Regex对象

```
import scala.io.Source
val source = Source.fromFile("myfile.txt", "UTF-8")
val lineIterator = source.getLines // 结果是一个迭代器
for (l <- lineIterator) print l
// or toArrary or toBuffer
// val lines = source.getLines.toArray
// or a single string
// val contents = source.mkString
source.close
```

```
// 正则表达式
val numPattern = "[0-9]".r
// 如果正则表达式包含反斜杠或引号
val wsnumwsPattern = """\s+[0-9]+\s+""".r

// findAllIn 遍历所有匹配项的迭代器
for (matchString <- numPattern.findAllIn("99 bottles, 98 bottles"))
	// process matchString

// findFirstIn, findPrefixOf ...

// Regex Group
val numitemPattern = "([0-9]+) ([a-z]+)".r
// 要匹配组，可以把正则表达式对象当做“提取器”使用
val numitemPattern(num, item) = "99 bottles"
// num = "99", item = "bottles"
```


## Trait (类似Java的接口)

> TODO  trait 是做什么的？
> TODO 笔记

*	类可以实现任意数量的特质
*	特质可以要求实现它们的类具备特定的字段、方法或超类
*	和Java接口不同，Scala特质可以提供方法和字段的实现
*	当你将多个特质叠加在一起时，顺序很重要——其方法被执行的特质排在更后面。

当做接口使用的特质：


## 操作符

操作符通常用来构建领域特定语言。隐式转换是另一个我们在创建领域特定语言时用到的工具。scala可以定义任意的操作符。

*	标识符(变量、函数、类等的名称)由字母、数字或运算符构成
*	一元和二元操作符其实是方法调用
*	操作符优先级取决于第一个字符，而结合性取决于最后一个字符。
*	apply和update方法在对expr(args)表达式求值时被调用
*	提取器从输入中提取元组或值得序列

apply和update方法：

> TODO 笔记

## 高阶函数

> TODO 笔记

*	匿名函数
*	但函数参数的函数
*	闭包
*	操作代码块的函数看上去就像是內建的控制语句。

我们可以在变量中存放函数:

```
import scala.math._
val num = 3.14
val fun = ceil _ // ceil _ 指的是函数本身
fun(3.14)
```

### 匿名函数

```
(x: Double) => 3 * x 

// 相当于
def fun(x: Double) = 3 * x

// 匿名函数可以直接传递给另一个函数
// 将每个元素乘以3
Array(3.14, 1.42, 2.0).map((x: Double) => 3 * x)
```

### 参数为函数的函数定义

```
// valueAtOneQuater的参数是一个接受Double并返回Double的函数
def valueAtOneQuater(f: (Double) => Double) = f(0.25)
```

valueAtOneQuater的类型是：
```
// (参数类型) => 结果类型
( (Double) => Double ) => Double
```

由于valueAtOneQuater是一个接受函数参数的函数，因此被称作高阶函数(higher-order function)。

高阶函数也可以产出另一个函数：

```
def mulBy(factor: Double) = (x: Double) => factor * x
// 如 mulBy(3)返回函数 (x: Double) => 3 * x
```

### 柯里化(currying)

柯里化指的是将原来接受两个参数的函数变成新的接受一个参数的函数的过程。新的函数返回一个以原有第二个参数作为参数的函数。示例：
```
// 如下函数接受两个参数
def mul(x: Int, y: Int) = x * y
// 以下函数接收一个参数，生成另一个接受单个参数的函数：
def mulOneAtATime(x: Int) = (y: Int) => x * y
// 计算两个数的乘积，其实mulOneAtATime(6)返回一个函数 (y: Int) => 6 * y
mulOneAtATime(6)(7)
// scala支持如下简写来定义这样的柯里化函数：
def mulOneAtATime(x: Int)(y: Int) = x * y
```



## Collection

> TODO 笔记

*	所有collection都扩展自Iterable trait
*	collection有三大类，分别为Seq、Set、Map
*	对于几乎所有collection类，Scala都同时提供了可变和不可变的版本
*	Scala 列表要么是空的，要么拥有一头一尾，其中尾部本事又是一个列表
*	Set是无先后次序的集合
*	用LinkedHashSet来保留插入顺序，或者用SortedSet来按顺序进行迭代
*	+将元素添加到无先后次序的集合中；+:和:+向前或向后追加到序列；++将两个集合串接在一起；-和--移除元素。
*	Iterable和Seq trait有数十个用于常见操作的方法。在编写冗长繁琐的循环之前，先看看能否满足你的要求
*	map、fold和zip操作示很有用的技巧，用来将函数或操作应用到集合中的元素。


## 模式匹配和样例类

Scala有一个十分强大的模式匹配机制，可以应用在很多场合：switch语句、类型查询，以及“析构”（获取复杂表达式中不同部分）。除此之外，Scala还提供了样例类，对模式匹配进行优化。

*	match表达式是一个更好的switch，不会有意外掉入到下一个分支的问题。
*	如果没有模式能够匹配，会抛出MatchError。可以用case _模式来避免。
*	模式可以包含一个随意定义的条件，称作守卫。
*	你可以对表达式的类型进行匹配；优先选择模式匹配而不是isInstanceOf/asInstanceOf。
*	你可以匹配数组、元组和样例类的模式，然后将匹配到的不同部分绑定到变量。
*	在for表达式中，不能匹配的情况会被安静地跳过。
*	样例类是编译器会为之自动产出模式匹配所需要的方法的类。
*	样例类继承层级中的公共超类应该是sealed的。
*	用Option来存放对于可能存在也可能不存在的值——这比null更安全。

```
var sig = ...
val ch: Char = ...

ch match {
	case '+' => sign = 1
	case '-' => sign = -1
	case _ => sign = 0
}
```

> scala 设计理念：if，for, match这些都是表达式，而不是控制语句，表达式有值，所以能进行赋值操作

```
sign = ch match {
	case '+' => 1
	case '-' => -1
	case _ => 0
}
```

类型模式

```
obj match {
	// 匹配到的值被当做Int绑定到x
	case x: Int => x
	case s: String => Integer.parseInt(s)
	case _: BigInt => Int.MaxValue
	cae _ => 0
}
```

匹配数据、列表和元组

```
// 匹配数组
arr match {
	// 匹配包含0的数组
	case Array(0) => "0"
	// 匹配任何带有两个元素的数组，并将这两个元素分别绑定到x,y
	case Array(x, y) => x + " " + y
	// 匹配任何以0开始的数组
	case Array(0, _*) => "0 ..."
	case _ => "something else"
}

// 匹配列表
lst match {
	case 0 :: Nil => "0"
	case x :: y :: Nil => x + " " + y
	case 0 :: tail => "0 ..."
	case _ => "something else"
}

// 匹配元组
pair match {
	case (0, _) => "0 ..."
	case (y, 0) => y + " 0"
	case _ => "neither is 0"
}
```

请注意变量时如何绑定到列表或元组的不同部分的。由于这种绑定让你可以很轻松地访问复杂结构的各组成部分，因此这样的操作被称为“析构”。

模式匹配的语法结构

```
<被匹配的对象> match {
	case <模式> => <match表达式的结果>
	case ...
} 

// 或者:
<被匹配的对象> match {
	// 模式匹配后，将表达式结果赋值给变量
	case <模式> => <变量> = <match表达式的结果>
	case ...
} 

// 或者:
<被匹配的对象> match {
	// 模式匹配后，将表达式结果赋值给变量
	case <变量>: <模式> => <match表达式的结果>
	case ...
}
```

提取器：模式匹配背后的原理

匹配数组、列表、元组的模式，其背后的原理是`提取器(extractor)机制`——带有从对象中提取值得unapply或unapplySeq方法的对象。

```
arr match {
	case Array(0, x) => ...
}

// Array伴生对象就是一个提取器——它定义了一个unapplySeq方法。Array.unapplySeq(arr)第一个值与零进行比较，而第二个值被赋值给x。

正则表达式使用提取器的例子：
val pattern = "([0-9]+) ([a-z]+)".r
"99 bottles" match {
	case pattern(num, item) => ...
	// num = 99, item = "bottles"
}
```

变量声明中的模式：

```
val (x, y) = (1, 2)
// 数组的第一个和第二个元素分别赋值给first, second
val Array(first, second, _*) = arr
```

## 泛型

> TODO: notes

> 用相同的逻辑操作不同类型的对象，是一种代码复用的方式。


## Actor

actor提供了一种比传统的加锁和线程处理更简单的并发模型。在用actor设计容错的高性能系统时推荐使用Akka库。

> 改为学习Akka

## 隐式转化和隐式参数

*	隐式转换用于类型之间做转换
*	你必须引入隐式转换，并确保它们可以以单个标识符的形式出现在当前作用域
*	隐式转换参数列表会要求指定类型的对象。它们可以从当前作用域中以单个标识符定义的隐式对象获取，或者从目标类型的伴生对象获取。
*	如果隐式参数是一个单参数的函数，那么它同时也会被作为隐式转换使用

### 隐式转换函数

以implicit 关键字声明的带有单个参数的函数。这样的函数被自动（隐式地）应用，将值从一种类型转换为另一种类型。

```
// example 1:
implicit def int2Fraction(n: Int) = Fraction(n, 1)

val result = 3 * Fraction(4, 5) // 实际执行为int2Fraction(3) * Fraction(4, 5)

// example 2: 如何让java.io.File能有个read方法来读取文件？如：
// val contents = new File("README").read
// 在Scala中，你可以定义一个经过丰富的类型，提供你想要的功能：
class RichFile(val from: File) {
	def read = Source.fromFile(from.getPath).mkString
}

implicit def file2RichFile(from: File) = new RichFile(from)
// 现在可以在对象上调用read方法了，它被隐式地转换成了RichFile
```

引入隐式转换函数:
*	位于源或目标类型的伴生对象中的隐式函数
*	位于当前作用域可以以单个标识符指代的隐式函数。
```
// 假定我们把int2Fraction函数放到位于com.horstmann.impatient包中的FractionConversions对象中，引入如下：
import com.horstmann.impatient.FractionConversions._

// 可以将引入局部化避免不想要的转换
object Main extends App {
	import com.horstmann.impatient.FractionConversions._
	val result = 3 * Fraction(4, 5)
	println(result)
}
```

### 隐式转换规则：

隐式转换在如下三个各不相同的情况会被考虑：

*	当表达式的类型与预期的类型不同时：

```
// 将调用fraction2Double, 因为sqrt预期的是一个Double
sqrt(Fraction(1, 4))
```

*	当对象访问一个不存在的成员时：

```
// java.io.File
new File("README").read
// 将调用file2RichFile, 因为File没有read方法
```

*	当对象调用某个方法，而该方法的参数声明与传入参数不匹配时：

```
// 将调用int2Fraction，因为Int的*方法不接受Fraction作为参数
3 * Fraction(4, 5)
```

使用如下参数编译可以看到编译器使用了哪些隐式转换：
```
scalac -Xprint:typer MyProg.scala
```

### 隐式参数：

函数或方法可以带有一个标记为implicit的参数列表。这种情况下，编译器将会查找缺省值，提供给该函数或方法。

```
case class Delimiters(left: String, right: String)

// quote这个函数是“柯里化的”
def quote(what: String)(implicit delims: Delimiters) = delims.left + what + delims.right
// 可以用显示的Delimiters对象来调用quote方法
quote("Hello")(Delimiters("<<", ">>"))
// 返回<<Hello>>

//也可以略去隐式参数列表：
quote("Hello")
// 在这种情况下，编译器将会查找一个类型为Delimiters的隐式值。这必须是一个被声明为implicit的值。编译器将会在如下两个地方查找这样的一个对象：
// (1)在当前作用域所有可以用单个标识符指代的满足类型要求的val和def
// (2)与所要求类型相关联的类型的伴生对象。
object FrenchPunctuation {
	implicit val quoteDelimiters = Delimiters("<<", ">>")
	...
}
```

### 利用隐式参数进行隐式转换

隐式的函数也可以被用做隐式转换。考虑如下泛型函数：

```
def smaller[T](a: T, b:T) = if (a < b) a else b
```

实际上，编译器不会接受这个函数，因为它并不知道a和b属于一个带有<操作符的类型。我们可以通过提供一个转换函数来达到目的：

```
def smaller[T](a: T, b: T)(implicit order: T => Ordered[T]) = if (order(a) < b) a else b
```

 由于Ordered[T] trait有一个接受T作为参数的<操作符，因此这个版本是正确的。
注意order是一个带有单个参数的函数，被打上了implicit标签，并且有一个以单个标识符出现的名称。因此，它不仅是一个隐式参数，还是一个隐式转换。因此，我们可以在函数体内略去order的显示调用：

```
def smaller[T](a: T, b: T)(implicit order: T => Ordered[T]) = if (a < b) a else b
```


---

## Q & A

**Q1:	val vs var vs def**
**A1:**

**Q2:	new in scala ?**
**A2:**

**Q3: Scala 为什么高并发 ?**
**A3:**

**Q4: class vs object ?  class extends vs object extends**
**A4:**

**Q5:public, protected, private when, why ?**
**A5:**

**Q6:什么是Actor并发模型？**
**A6:**

--

## References

1.《快学Scala》

用最精简的语言讲解最基础的内容，适合入门，里面的题目可以认真完成。

2.	Run Scala Online

http://www.tutorialspoint.com/compile_scala_online.php

3.	关于Actor Model 和 Akka的8篇文章

http://rerun.me/

4.	Actor Model

https://en.wikipedia.org/wiki/Actor_model

5.	Akka官方关于Actor的整体介绍

http://doc.akka.io/docs/akka/2.4.2/general/index.html


> Written with [StackEdit](https://stackedit.io/).