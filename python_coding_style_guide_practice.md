# python coding style guide 的落地实践

> 本文我想表达的是：机器和人各有所长，适合机器做程序化、自动化的事无须人代劳，例如我下面要介绍的使用flake8 对python代码做 coding style 检查。

## PEP8 & Flake8

PEP 8: https://www.python.org/dev/peps/pep-0008/

https://flake8.readthedocs.org
Warning / Error codes: https://flake8.readthedocs.org/en/latest/warnings.html

```
# Installation

pip install flake8
pip install pep8-naming
pip install flake8-import-order
pip install flake8-todo
pip install flake8-respect-noqa
```

检查安装了哪些插件： 

```
$ flake8 --version
```

配置(global level)：
The user settings are read from the ~/.config/flake8 file (or the ~/.flake8 file on Windows). 

vim ~/.config/flake8

```
[flake8]
ignore = E201,E202,E302
exclude = .tox,*.egg
max-line-length = 120
max-complexity = 10
application-import-names = pep8-naming,flake8_import_order,flake8-todo,flake8-respect-noqa
```

使用：
```
flake8 --show-source --import-order-style=google <project_dir_or_py_file>
```

## vcs hook

## 自动化测试


> Written with [StackEdit](https://stackedit.io/).