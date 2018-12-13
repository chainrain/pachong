"""
有些网站爬数据的时候会报这样的错
raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='www.numpy.org.cn', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:645)'),))
"""

import requests
# 使用requests请求不安全的证书网站

url = 'https://www.numpy.org.cn/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# 指定不启用证书认证: verify=False
response = requests.get(url, headers=headers,verify=False)

print(response.content.decode())
