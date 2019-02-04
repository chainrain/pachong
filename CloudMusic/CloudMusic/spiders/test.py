import requests



url = 'https://music.163.com/weapi/artist/list?csrf_token='

data = {
'params': 'tXvk/ih6pzfRnsytVrA7dTo/TydnpbxzWGAOPdd0GTZntMtJVeOZc5MDeX5uq9b419FQOaPaaQr/U34HcSPNouV3Ov0lC+UZm7vd6GQVdKJ43YV/H4bVdI5gGWG0kBjSsj1xEsCnOx2Fes2rkYEq/b5q+QcQ4kwkrEBXkMtLp0kmoEs5T5y79xWyZB4pIBcx',
'encSecKey': '57ed05c9d3940ad10f963ed39600c5b9304bf41bea4123bb3e39ec3dc2e0f52636c2ea20538357e3b5aface3642ad61aab49a6ad2274f34e12d7876b6b5d9153cc067bdb2f7706309bb51d68db136492b0f7da03461a0d2093e29e77c62a50c99e1a8b1e413ce893bc2b3f17d1c357e46d40a07c40b85577f410c7acfc819c75'
}


head = {

        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

}
head['cookie'] = 'Cookie: P_INFO=m18665625762_1@163.com|1542199361|0|other|00&99|gud&1542198232&other#gud&440100#10#0#0|186762&1|mail163&unireg|18665625762@163.com; _ntes_nnid=36f77d3fb8cbcd1310af34fe1c0983e0,1542199368974; _ntes_nuid=36f77d3fb8cbcd1310af34fe1c0983e0; WM_TID=1wDNx7xwXb9AERQUAFZoO0YcW7j8QXA%2B; _iuqxldmzr_=32; WM_NI=IHI6eqajfaDKH9GmN6bV6TtC9mhc1W4UUa0DP9fbMaTUg8i84QWqPnHik6b%2BopmQuhL0DEC%2FnBnBR9UjW0doeGgnBXr7dgsK%2FHoFmHgl0HCK6eM6cJBLflt4UAoaxxOmeWE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea8d93cb0bbfc8cc77d9bac8aa3c15a879e8babee748c91ae8cc9678fefa190fc2af0fea7c3b92a8b9887d7e87ba3b6aa82c7418ce7898ecd3ea28afab5f749fbb3a884b45df88b9b82b35094e7aa83d06b988ba9d9ec34f88f9992d3668cb7a5d7e121adb0a3b2f86490f08ca6c225ae9ea2a3d13397b699d1e765a799a98fc154b2e9ac88f241ed98a1a7f044a5b400a9c241f6bb83d7e2428294aa8df740979fa182fb748db3abb8c837e2a3; __utma=94650624.299544030.1547724038.1547724038.1547726507.2; __utmc=94650624; __utmz=94650624.1547726507.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=94650624.15.10.1547726507; JSESSIONID-WYYY=b1562OXa0XH2JN0y5pwDx6DPD0hYyEXdQn5hBWWgQq%5C7s4k5C4Iw93DHYUyK7qOW9zybNh4aGOWEfDjB4aRs2nhmAEGszY5%5C9cAmRWsF%5CVPDIAx%2B07JqksNvOFCM8JkJkTQZ%2B2C8Xf9dd%2By0VSnQZyBIFHCiglaTBgC0X6h8%5C4VsbunW%3A1547730089752'

# head['Cookie'] = 'JSESSIONID-WYYY=Jgi1ax6XAkd6cNwfV6qxBbhya5s4SW00PtEcYPNYUgdOeQO%5Cf%2FyFUQo%2FAVRlqDhDV8d7D%5CSGCtdu0NYgBxn9YdoZ0WuTb9VH0Nydug%2BZ4SUn74vDPG%2F%5CD6slP%2FmuljYfIVf%2F2X%5CxlrXuCvJjw8ER4amzfEPao6x5elWf%2B2OkzmGPJ%2Bvz%3A1515500969576; _iuqxldmzr_=32; _ntes_nnid=099805196f22bf7617cf11b5a67feeff,1515499169604; _ntes_nuid=099805196f22bf7617cf11b5a67feeff; __utma=94650624.1398381638.1515499170.1515499170.1515499170.1; __utmc=94650624; __utmz=94650624.1515499170.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=94650624.6.10.1515499170'

if __name__ == '__main__':

    url = 'http://music.163.com/weapi/v1/resource/comments/A_PL_0_2015321897?csrf_token='
    # url = 'http://music.163.com/weapi/v1/resource/comments/A_PL_0_973757368?csrf_token='
    s = requests.session()
    r = s.post(url,data=data,headers = head)
    print(r.text)
