"""
获取到已登录的界面
使用headers来携带cookie信息
"""

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Cookie': 'anonymid=joy885ykar59c0; depovince=GW; _r01_=1; ick_login=7130ca22-ade4-40ab-a1d8-666698a8327b; JSESSIONID=abc583MPV91RN9GttXpDw; ch_id=10016; first_login_flag=1; ln_uact=18665625762; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=70ec7a38-6228-45cb-a940-d5c50dafbdde%7C7142c2896cba1335a36727e867985d46%7C1543231639433%7C1%7C1543231638911; wp_fold=0; XNESSESSIONID=beda8cfa6f65; WebOnLineNotice_901245995=1; jebecookies=72d6a43d-6a82-432c-a821-06a59a3d00fa|||||; _de=9DC89EDDF9DCFBD97D25666AD7245648; p=f2dc8f87da8d77e719a8e3190bf325c65; t=b105b0690189576bb365a6ba7b6ea1215; societyguester=b105b0690189576bb365a6ba7b6ea1215; id=901245995; xnsid=b026ca69; loginfrom=syshome'
}
"""
这个url可以是别人的,也可以是自己的
自己的话访问自己主页
别人的话,自己的账户访问别人的主页
"""
# url = 'http://www.renren.com/965194180/profile'  # 老师的主页
url = 'http://www.renren.com/901245995/profile'  # 我的主页


response = requests.get(url, headers=headers)

print(response.content.decode())

