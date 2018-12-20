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

# 转为_Element对象
print(element)
print(type(element))

# 拿到页面
print(etree.tostring(element))  # 二进制版
print(etree.tostring(element).decode())  # 解码后恢复正常