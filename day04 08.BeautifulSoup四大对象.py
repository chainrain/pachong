from bs4 import BeautifulSoup
"""
安装: pip3 install bs4
"""

# 准备html字符串数据
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 创建BeautifulSoup对象, 代表整个文档
# 报警告原因: 我们没有指定解析器,解析方案: 指定解析器
bs = BeautifulSoup(html,'lxml')
print(type(bs))      # <class 'bs4.BeautifulSoup'>  整体,bs4.BeautifulSoup类型


title = bs.title
# title元素
print(title)         # <title>The Dormouse's story</title>
# 元素标签类型
print(type(title))   # <class 'bs4.element.Tag'>
# class=title的文本
print(title.text)    # The Dormouse's story


p = bs.p
# 获得第一个p标签的class
print(p.get('class'))
# 获得第一个p标签的所以属性
print(p.attrs)

# 是str的扩展类, 1. 字符串的功能 2.查找元素
print(bs.b.string)
print(type(bs.b.string))  # bs4.element.NavigableString类：表示HTML中标签的文本（非属性字符串）。

# 获取父节点
print(bs.b.string.find_parent())

# 4. bs4.element.Comment类：表示标签内字符串的注释部分，是一种特殊的NavigableString对象。
print(bs.a.string)
print(type(bs.a.string))