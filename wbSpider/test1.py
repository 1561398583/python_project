import requests
from bs4 import BeautifulSoup

url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml"
res = requests.get(url)
#因为返回的res的head中没有编码，默认按照ISO8890编码来处理，有中文就会出现乱码，所以这里手动设置编码为utf-8
res.encoding = "utf-8"
#text是Response的一个function，被@property装饰为一个属性，text会根据encoding返回相应解码后的string
html = res.text

#解析html
soup = BeautifulSoup(html)



print(html)