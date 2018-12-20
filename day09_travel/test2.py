import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
url = 'http://www.gzl.com.cn/grouptour/scheduleDateMap.json'
data = {'pdId':'0F1ACAEBF8C441DDE0532429030A5D63'}

index = requests.post(url=url,data=data,headers=headers)
# print(index.content.decode())

url2 = 'http://www.gzl.com.cn/search/all/xianggelila.html'
response = requests.get(url=url2,headers=headers)
print(response.content.decode())