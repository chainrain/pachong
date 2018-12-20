import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}


url = 'http://www.gzl.com.cn/domestic/0F1ACAEBF8C441DDE0532429030A5D63.html'

da = requests.get(url,headers=headers)

print(da.content.decode())

print(re.findall("pdId: '(.*?)",da.content.decode()))


data = {
'pdId': '0F1ACAEBF8C441DDE0532429030A5D63',
'schdId': '40288022670c007f01671be757eb25ad',

'adultNum': 1,
'childNum': 0,
'babyNum': 0,
'travelDays': 6,
'departureDate': '2018-12-20',
'isFreeShuttle': 0,
'isShowShuttle':0,
}

da = requests.post(url = 'http://www.gzl.com.cn/grouptour/findScheduleInfo.shtml',data = data,headers=headers)


a = da.content.decode()

import re
data = re.findall(r"priceText.*?\.html(.*?);",a)
#$("#priceText").html('3999');
print(data[0][2:-2])
print(data)