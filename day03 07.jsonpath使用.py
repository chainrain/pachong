"""
JsonPath: 是一个根据路径定位json中数据的工具, 可以说JsonPath是json中的XPATH,相当于搜索引擎
jsonpath不能直接处理json格式字符串, 只能处理由json格式的字符串转换后的python类型
"""
from jsonpath import jsonpath
import json

json_str = '''
{ "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
'''

# 1. 把json的字符串转换为python类型的数据
data = json.loads(json_str)
# print('把json的字符串转换为python类型的数据',data)

book = jsonpath(data,'$.store.book')
print('获取所有的书',book)

author = jsonpath(data,'$.store.book[*].author')
print('获取作者,方式1',author)

author1 = jsonpath(data, '$..author')
print('获取作者方式2,从根节点开始, 无论位置在哪里, 只要是节点名author的值全部放到列表中返回',author1)

price = jsonpath(data,'$..price')
print('获取所有价格',price)

second_book = jsonpath(data,'$..book[1]')
print('第二本书(索引从0开始)',second_book)

first_third_book = jsonpath(data,'$..book[0,2]')
print('第一和第三本书',first_third_book)

last_book = jsonpath(data,'$..book[-1:]')
# last_book = jsonpath(data, '$..book[(@.length-1)]')
print('最后一本书',last_book)

first_to_third_book = jsonpath(data,'$..book[0:3]')
print('第一到第三本书',first_to_third_book)

isbn = jsonpath(data,'$..book[?(@.isbn)]')
print('带有isbn属性的书',isbn)

price_smaller_than_10 = jsonpath(data,'$..book[?(@.price<10)]')
print('获取价格小于10的书',price_smaller_than_10)