import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

word = input('搜索内容')

"""方案1:拼接url"""
# url = 'https://www.baidu.com/s?wd={}'.format(word)  # format把数值放到大括号里面,不用像%指定数据类型
#
# response = requests.get(url=url,headers=headers)
# print(response.content.decode())
# print(response.request.headers)

"""方案2:使用params参数(requests包自带的params=方法)"""
# url = 'https://www.baidu.com/s'
# params = {
#     'wd':word
# }
# response = requests.get(url,params=params,headers=headers)
# print(response.content.decode())
# print(response.request.headers)