
import requests

# 发送请求, 获取响应数据
response = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1543736687&di=571a3643e8865b6b1af8f4a0f9b0f062&imgtype=jpg&er=1&src=http%3A%2F%2Fwww.deyu.ln.cn%2Fimages%2Foazs43lvonuwglrrgi3c43tfoq%2F-T9z7-ml37DpTYY34Pvhxg%3D%3D%2F1365593503199696.jpg')

# 把图片写入文件中,图片需要用wb写入,不要用w写入
with open('a.jpg', 'wb') as f:
    f.write(response.content)
    print('完成')
