from bs4 import BeautifulSoup
import re

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
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
'''


# 1. 创建BeautifulSoup对象
bs = BeautifulSoup(html, 'lxml')


"""
find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs)
name: 根据标签名进行查找
attrs: 根据属性进行查找
recursive: True, 找所有后代节点,如果是False只查找子节点
kwargs: 根据属性进行查找
"""
index= bs.find()
print(index)

p_s = bs.find_all(name='p')
# print('name = p_s',p_s)

b_s = bs.find_all(re.compile('^b'))
# print(b_s)

ab_s = bs.find_all(['a','b'])
# print(ab_s)

sister = bs.find_all(class_='sister')
# print(sister)

value = bs.find_all(attrs={'data-foo':'value'})
# print(value)

foo = bs.find_all(text='foo!')
# print(foo)

lacie = bs.find_all(text=['Lacie','Tillie'])
# print(lacie)
