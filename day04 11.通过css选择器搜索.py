from bs4 import BeautifulSoup

html = '''
   <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
    <body>
    <div data-foo="value">foo!</div>
    <p class="title" name="dromouse">
        <b>The Dormouse's story</b>
    </p>
    <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister link3" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
'''

# 1. 创建BeautifulSoup对象
bs = BeautifulSoup(html, 'lxml')

# print('a标签',bs.select('a'))
# print(' sister类 ',bs.select('.sister'))

# print('id为link1',bs.select('#link1'))

# print('后代节点',bs.select('p b'))

# print('子节点',bs.select('p > b'))

# print('id为link1的a标签',bs.select("a[id='link1']"))

# print('多个class查询',bs.select('.sister.link3'))