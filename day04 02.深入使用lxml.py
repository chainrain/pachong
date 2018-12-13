"""
lxml的使用:
安装:pip install lxml

"""
from lxml import etree  # 这个etree,pycharm可能回找不到,但是只要安装了,就不影响使用


html = '''
<div> <ul>
<li class="item-1"><a href="link1.test">first item</a></li>
<li class="item-1"><a href="link2.test">second item</a></li>
<li class="item-inactive"><a href="link3.test">third item</a></li>
<li class="item-1"><a href="link4.test">fourth item</a></li>
<li class="item-0"><a href="link5.test">fifth item</a>
</ul> </div>
'''

# HTML具有自动修正html的功能,注意: 在修正时候可能会改变文档结构, 可能会导致你XPATH无效.
element = etree.HTML(html)

# 拿到class为"item-1"的a标签的文本
texts = element.xpath('//li[@class="item-1"]/a/text()')
print(texts)
# 拿到class为"item-1"的a标签的链接
hrefs = element.xpath('//li[@class="item-1"]/a/@href')
print(hrefs)

# 对数据进行一个简单合并, 'first item', 'link1.h0x7f693cdcba60tml' 在一起
# 注意通过索引进行匹配的时候, 如果某个值没有的话,可能会导致数据错乱.
for text in texts:
    item = {}
    item['text'] = text
    # print(text.index)
    item['href'] = hrefs[texts.index(text)]  # 按照索引分配href,print(hrefs[1])
    print(item)
