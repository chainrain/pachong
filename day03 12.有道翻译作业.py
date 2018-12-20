"""
1.打开
http://fanyi.youdao.com/

2.发起请求,找到请求translate_o?smartresult=dict&smartresult=rule,看看请求的Initiator用到哪个js,点进js,找到callstack,找到t.translate.

3.这是发起的请求,salt: r.salt,sign: r.sign,这两个值分别是从r得到:r = g.generateSaltSign(n),点进去函数
    t.translate = function(e, t) {
        _ = f("#language").val();
        var n = x.val()
          , r = g.generateSaltSign(n)
          , i = n.length;
        if (F(),
        T.text(i),
        i > 5e3) {
            var a = n;
            n = a.substr(0, 5e3),
            r = g.generateSaltSign(n);
            var s = a.substr(5e3);
            s = (s = s.trim()).substr(0, 3),
            f("#inputTargetError").text("有道翻译字数限制为5000字，“" + s + "”及其后面没有被翻译!").show(),
            T.addClass("fonts__overed")
        } else
            T.removeClass("fonts__overed"),
            f("#inputTargetError").hide();
        d.isWeb(n) ? o() : l({
            i: n,
            from: C,
            to: S,
            smartresult: "dict",
            client: k,
            salt: r.salt,
            sign: r.sign,
            doctype: "json",
            version: "2.1",
            keyfrom: "fanyi.web",
            action: e || "FY_BY_DEFAULT",
            typoResult: !1
        }, t)
    }

4.这是两个变量的值
    var r = function(e) {
        var t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
        return {
            salt: t,
            sign: n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")
        }
"""
import hashlib
import random
import time
import requests
from jsonpath import jsonpath

# 翻译URL
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

# 必要的一些请求头参数
headers = {
    'Cookie':'OUTFOX_SEARCH_USER_ID=-1150500769@10.168.8.63; JSESSIONID=aaaHD8dYJlGCLdvstFADw; OUTFOX_SEARCH_USER_ID_NCOO=212815704.32119665; ___rl__test__cookies=1543411428093',
    'Referer':'http://fanyi.youdao.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2601.400'
}

# 内容
word = input('请输入需要查询的内容')

# salt值
salt = int(time.time()*1000) + random.uniform(1,10)

# sign值
sign = "fanyideskweb" + word + str(salt) + "sr_3(QOHT)L2dx#uuGR@r"

# md5加密
sign = hashlib.md5(sign.encode()).hexdigest()


# 'action': "FY_BY_DEFAULT",
data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action':  'FY_BY_DEFAULT',
            'typoResult': False,
        }

response = requests.post(url=url,data=data,headers=headers)
# print(response.content.decode())

result = jsonpath(response.json(),'$..tgt')[0]
print(result)