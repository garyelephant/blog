# python coding style guide 的快速落地实践

---

> 机器和人各有所长，如coding style检查这种可自动化的工作理应交给机器去完成，故发此文帮助你在几分钟内实现coding style的自动检查。

---

## 1.有哪些著名的Python Coding Style Guide

*	PEP8

https://www.python.org/dev/peps/pep-0008/

发明Python语言丰碑人物Guido van Rossum的亲自写的Coding Style, 知名度5颗星，可操作性5颗星。

* Google Python Coding Style Guide

http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

Google内部广泛使用Python作为开发语言，此Coding Style 在坊间流传很广，知名度5颗星，可操作性5颗星。值得一提的是Guido也曾经在Google工作过一段时间。


## 2.Flake8 - Coding Style检查`自动化`的利器

你可能听说过[pep8](https://github.com/PyCQA/pep8)，这是一个根据`PEP8`规范检查python代码style的自动化工具。[`flake8`](https://flake8.readthedocs.org)是对`pep8`进行了包装，充分发挥了插件化的优势，增加了如代码复杂度，函数、变量命名习惯，import顺序等检查。

### 2.1 安装Flake8

安装flake8，同时安装一些有用的插件。

*	pep8-nameing

https://github.com/PyCQA/pep8-naming
命名检查

*	flake8-import-order

https://github.com/public/flake8-import-order
import 顺序检查，可以有两种风格顺序检查cryptography, google。如`google`的意思是import顺序是（1）标准库（2）第三方库（3）本地项目库。代码检查时可以通过`--import-order-style=google`来指定。

*	flake8-todo

https://github.com/schlamar/flake8-todo
检查代码中的todo。

*	flake8-quotes

https://github.com/zheller/flake8-quotes/
检查单双引号的使用是否正确。

具体安装命令如下：

```
$ pip install flake8
$ pip install pep8-naming
$ pip install flake8-import-order
$ pip install flake8-todo
$ pip install flake8-quotes
```

检查安装了哪些插件： 
```
$ flake8 --version
# 输出如下内容，显示了已安装的插件：
2.5.1 (pep8: 1.5.7, import-order: 0.6.1, naming: 0.3.3, pyflakes: 1.0.0, mccabe: 0.3.1, flake8-todo: 0.4, flake8_quotes: 0.1.1) CPython 2.6.6 on Linux
```

### 2.2 用Flake8检查Python Codes

例如如下代码：
```
# test.py

from order import place_order
import os, sys

class website_api(object):
    def __init__(self):
        self.user_name = ''
        self.Gender = 'male'
        #comment in wrong ident
        self.active =False

    def login(self, Person):
        self.user_name=Person.user_name
        not_used_var = 0
        return True

    def Logout(self):
        self.active =False

    def place_order(self):
        place_order()

def action():
    Client_a = website_api()
    Client_a.login()
    Client_a.place_order()
    Client_a.Logout()
```

执行检查命令：
```
$ flake8 --first --import-order-style=google test.py
```

输出结果如下，你可以根据错误码来修正代码，如其中的`N802`的意思是function name不应该包含大写英文字母。

```
# flake8 output
test.py:2:1: F401 'sys' imported but unused
test.py:2:1: I100 Imports statements are in the wrong order. from os, sys should be before from order
test.py:2:1: I201 Missing newline before sections or imports.
test.py:2:10: E401 multiple imports on one line
test.py:4:7: N801 class names should use CapWords convention
test.py:8:9: E265 block comment should start with '# '
test.py:9:22: E225 missing whitespace around operator
test.py:11:9: N803 argument name should be lowercase
test.py:13:9: F841 local variable 'not_used_var' is assigned to but never used
test.py:16:9: N802 function name should be lowercase
test.py:23:5: N806 variable in function should be lowercase
```

除此之外，flake8也可以递归得检查某个目录中的代码：

```
$ flake8 your_project_dir
```

flake8常用的options有：

*	--show-source

show source code for each error

*	--first

show first occurrence of each error

*	--import-order-style=google

import order style to follow

*	--count

print total number of errors and warnings to standard error and set exit code to 1 if total is not null

*	--help

get help

### 2.3 Flake8 Warning / Error codes 列表

| Codes | Notes | Link |
| ------ | ------ | ------ |
| E\*\*\*/W\*\*\* | pep8 errors and warnings | http://pep8.readthedocs.org/en/latest/intro.html#error-codes |
| F\*\*\* | PyFlakes codes (see below) | https://flake8.readthedocs.org/en/latest/warnings.html |
| C9\*\* | McCabe complexity, 目前只有C901 | https://github.com/PyCQA/mccabe |
| N8\*\* | PEP-8 naming conventions | https://github.com/PyCQA/pep8-naming#plugin-for-flake8 |
| I\*\*\* | checks the ordering of your imports | https://github.com/public/flake8-import-order#warnings |
| T\*\*\* | 目前只有T000检查代码中是否包含TODO, FIXME | https://github.com/schlamar/flake8-todo |
| Q\*\*\* | 目前有Q000代表单双引号使用错误 | https://github.com/zheller/flake8-quotes/ |

随着新的flake8 plugin的集成，还可能有其他的codes，如果你的项目有特殊的代码检查需求，也可开发自己的plugin。


### 2.4 Flake8的个性化配置

根据需要，flake8的配置可以是全局的(对所有project有效)，也可以是分project的。这里仅举例说明全局配置方法，分project配置请见[flake8 Per Project Configuration](https://flake8.readthedocs.org/en/latest/config.html#per-project)。

编辑 `~/.config/flake8`

```
[flake8]
ignore = E201,E202,E302
exclude = .tox,*.egg
max-line-length = 120
```

以上配置的意思是flake8不检查E201, E202, E302这三个错误，不检查.tox,*.egg文件，允许的最长单行代码长度为120个字符。


### 2.5 Flake8高级用法 - Git Commit Hook

flake8可结合Git实现`commit`时检查coding style的目的，如果flake8报错，则无法`commit`。

在python project的根目录下执行如下命令安装git pre-commit hook。
```
$ flake8 --install-hook
$ git config flake8.strict true
```


---

## References

1.	PEP8
https://www.python.org/dev/peps/pep-0008/

2.	Google Python Coding Style
http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

3.	pep8工具
https://github.com/PyCQA/pep8

4. flake8
https://flake8.readthedocs.org

5.	Warning / Error codes of flake8
https://flake8.readthedocs.org/en/latest/warnings.html


---

> Written with [StackEdit](https://stackedit.io/).