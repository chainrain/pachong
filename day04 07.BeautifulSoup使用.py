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
print(bs)