"""
爬虫面试题: 青海省招标公告
http://www.qhggzyjy.gov.cn/ggzy/jyxx/001001/001001001/secondPage.html
这个页面的源码是没有数据的,要在开发者界面,network有个getFullTextData的post请求,那里才有数据

"""
import requests

url = 'http://www.qhggzyjy.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# 直接用json作为data会请求失败,因为data里面有转义符 \
# data = '{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001;002;003;004;005;006;007;008;009;010","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":true,"likeType":2,"equal":"001001001"}],"time":null,"highlights":"title","statistics":null,"unionCondition":null,"accuracy":"100","noParticiple":"0","searchRange":null,"isBusiness":1}'
data = r'{"token":"","pn":0,"rn":10,"sdt":"","edt":"","wd":"","inc_wd":"","exc_wd":"","fields":"title","cnum":"001;002;003;004;005;006;007;008;009;010","sort":"{\"showdate\":\"0\"}","ssort":"title","cl":200,"terminal":"","condition":[{"fieldName":"categorynum","isLike":true,"likeType":2,"equal":"001001001"}],"time":null,"highlights":"title","statistics":null,"unionCondition":null,"accuracy":"100","noParticiple":"0","searchRange":null,"isBusiness":1}'
response = requests.post(url=url,data=data,headers=headers)
print(response.content.decode())