import requests
from bs4 import BeautifulSoup
import time

#抓取企查查四川数据
base_url = 'https://www.qcc.com/g_SC_510100_'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding' : 'gzip, deflate, br',
    'accept-language' : 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cookie' : 'UM_distinctid=17a70797b303b0-0929cb8a9f5b67-6373267-100200-17a70797b31596; QCCSESSID=amkv8kae564sompbb1hs1jf6q5; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201627274378801%2C%22updated%22%3A%201627274400200%2C%22info%22%3A%201627274378806%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E4%BC%81%E6%9F%A5%E6%9F%A5%E7%BD%91%E7%AB%99%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.google.com.hk%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%22undefined%22%7D; CNZZDATA1254842228=1909718359-1625381967-https%253A%252F%252Fwww.google.com.hk%252F%7C1629444050; acw_tc=744d4a0f16294490796105115eeee9b2304cd93cea289ef679977526c7; zg_did=%7B%22did%22%3A%20%2217a707985611de-0e7ad50ae1b1e6-6373267-100200-17a707985622bf%22%7D; zg_294c2ba1ecc244809c552f8f6fd2a440=%7B%22sid%22%3A%201629446975194%2C%22updated%22%3A%201629449080123%2C%22info%22%3A%201628928664970%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22cuid%22%3A%20%22undefined%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201629446975194%7D',
    'referer' : 'https://www.qcc.com/g_SC_510100_10',  #这个动态变化
    'upgrade-insecure-requests' : '1',
}

'''
获取一页并解析
pageNum: 页数
首先，HTML 文档将被转换成 Unicode 编码格式，
然后 Beautiful Soup 选择最合适的解析器来解析这段文档，此处指定 lxml 解析器进行解析。
解析后便将复杂的 HTML 文档转换成树形结构，并且每个节点都是 Python 对象。
这里将解析后的文档存储到新建的变量 soup 中
'''
def getOnePageData(pageNum):
    url = base_url + str(pageNum)
    strhtml = requests.get(url, headers=headers)  # Get方式获取网页数据
    # 更新refer
    headers['referer'] = url
    soup = BeautifulSoup(strhtml.text, 'lxml')
    #接下来用 select（选择器）定位数据,获取每页的所有公司
    cs = soup.select('#searchlist > table > tbody > tr')
    csInfos = []
    for item in cs:
        # 获取一个公司的信息
        aInfo = getOneCompanyData(item)
        csInfos.append(aInfo)

    return csInfos


'''
获取每一个公司的信息
company:一个公司的soup
'''
def getOneCompanyData(company):
    # 获取第二个和第三个td子节点
    a1 = company.select('td:nth-child(2) > a')[0]
    companyName = a1.get_text()  # 公司名字
    isr = isHaveStr(companyName)
    if isr == False:
        return False
    href = a1['href']   #公司连接
    # 老板名字
    bossName = company.select('td:nth-child(2) > p:nth-child(3) > a')[0].string
    # 成立时间
    #createDate = company.select('td:nth-child(2) > p:nth-child(3) > span:nth-child(3)')[0].string
    # 地址
    addr = company.select('td:nth-child(2) > p:nth-child(5)')[0].string
    #状态
    status = company.select('td.statustd > span')[0].string
    #获取其他信息
    otherInfo = getCompanyInfo(href)

    result = {
      'companyName' : companyName,
      'bossName' : bossName,
      'addr' : addr,
      'status' : status,
      'during' : otherInfo['during'],
      'businessScope': otherInfo['businessScope']
    }

    return result

'''
公司主页的信息
rurl:相对url
'''
def getCompanyInfo(rurl):
    url = 'https://www.qcc.com' + rurl
    strhtml = requests.get(url, headers=headers)  # Get方式获取网页数据
    soup = BeautifulSoup(strhtml.text, 'lxml')
    #时间
    during = soup.select('#cominfo > div:nth-child(2) > table > tr:nth-child(5) > td:nth-child(4)')[0].string
    #经营范围
    businessScope = soup.select('#cominfo > div:nth-child(2) > table > tr:nth-child(10) > td:nth-child(2)')[0].string
    time.sleep(3)
    return {'during' : during, 'businessScope' : businessScope}


'''
判断字符串s是否包含‘软件’、‘科技’、‘网络’、‘信息’
'''
def isHaveStr(s):
    if s.find('软件') != -1:
        return True
    if s.find('科技') != -1:
        return True
    if s.find('网络') != -1:
        return True
    if s.find('信息') != -1:
        return True
    return False