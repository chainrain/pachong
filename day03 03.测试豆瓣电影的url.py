"""

豆瓣网的所有电影的url
https://m.douban.com/rexxar/api/v2/subject_collection/movie_latest/items?os=android&callback=jsonp3&start=0&count=8&loc_id=108288&_=1543305804872
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'Referer':'https://m.douban.com/movie/nowintheater?loc_id=108288'
}

# 注意,要把callback删了,不然会有头部https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&callback=jsonp1&start=0&count=8&loc_id=108288&_=1543305804870
url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1543306858016'

response = requests.get(url,headers=headers)
print(response.content.decode())