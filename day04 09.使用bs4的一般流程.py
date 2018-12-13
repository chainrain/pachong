from bs4 import BeautifulSoup

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
bs = BeautifulSoup(html,'lxml')

print(bs)

# 得到a标签
a_s = bs.find_all('a')
for a in a_s:
    # 得到a标签的文本
    # print('a.text',a.text)
    # 得到a标签的链接
    # print('a.get href',a.get('href'))
    print(a.text,a.get('href'))