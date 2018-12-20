"""
lxml的使用:
安装:pip install lxml

"""
from lxml import etree  # 这个etree,pycharm可能回找不到,但是只要安装了,就不影响使用


html = '''
<div> <ul>
<li class="item-1"><a href="link1.test"></a></li>
<li class="item-1"><a href="link2.test">second item</a></li>
<li class="item-inactive"><a href="link3.test">third item</a></li>
<li class="item-1"><a>fourth item</a></li>
<li class="item-0"><a href="link5.test">fifth item</a>
</ul> </div>
'''

# HTML具有自动修正html的功能,注意: 在修正时候可能会改变文档结构, 可能会导致你XPATH无效.
element = etree.HTML(html)

# 先定位一条条的a标签
a_s = element.xpath('//li[@class="item-1"]/a')
print(a_s)

# 遍历a标签列表
for a in a_s:
    item={}
    item['text'] = a.xpath('./text()') if len(a.xpath('./text()')) != 0 else '没有text'  # 由标签找到对应的text,如果没找到,返回None
    item['href'] = a.xpath('./@href') if len(a.xpath('./@href')) != 0 else '没有href'  # 由标签找到对应的href
    print(item)
