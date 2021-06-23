# -*- coding = utf-8 -*-
# Software: PyCharm
# 姓名:闫瑀
# 时间:2021/6/8 0:46
import  urllib.request
#获取一个get请求
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
#获取一个post请求
# import  urllib.parse
# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read().decode('utf-8'))


#超时处理
# try:
#     response = urllib.request.urlopen('http://httpbin.org/post',timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print('time out')

# response = urllib.request.urlopen('http://www.baidu.com')
# #print(response.status)
# print(response.getheaders())
#url = 'http://www.douban.com'

# url = 'http://httpbin.org/post'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5977.400 LBBROWSER/10.1.3752.400'}
# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))



url = 'https://www.douban.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5977.400 LBBROWSER/10.1.3752.400'}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))