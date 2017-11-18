## docsify.js使用技巧：

(1) http://localhost:3000/#/zh-cn/ 与 http://localhost:3000/#/zh-cn 是完全不同的url, 前者会自动加载/zh-cn目录下面的README.md和_sidebar.md

(2) 中英文切换。
在根目录的_navbar.md配置：
```
- [中文](/zh-cn/)
- [En](/en/)
```

(3) 如何避免在多个目录存放同一个文件。
在index.html 用alias，例如希望每个页面都加载_navbar.md,但是不想在每个子目录都存放_navbar.md
```
alias: {
  '/.*/_navbar.md': '/_navbar.md',
},
```

(4) 希望引用外部的markdown文件

在alias里面配置。

(5) 如何在文档正文中创建指向站内的其他文档的链接

```
假设文档的结构如下：
# docs是文档的根目录
docs/
docs/zh-cn/README.md
docs/zh-cn/Guide.md

# 如果要在README.md中创建一个指向Guide.md的链接，写法是：
[Getting Started Guide](zh-cn/Guide.md)

```
