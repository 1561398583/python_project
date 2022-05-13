import requests
from bs4 import BeautifulSoup
import time

class QCC:
    def __init__(self, cookie):
        self.base_url = 'https://www.qcc.com/g_SC_510100_'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'referer': 'https://www.qcc.com/g_SC_510100_10',  # 这个动态变化
            'upgrade-insecure-requests': '1',
            'cookie': cookie
        }



    '''
    获取一页并解析
    pageNum: 页数
    首先，HTML 文档将被转换成 Unicode 编码格式，
    然后 Beautiful Soup 选择最合适的解析器来解析这段文档，此处指定 lxml 解析器进行解析。
    解析后便将复杂的 HTML 文档转换成树形结构，并且每个节点都是 Python 对象。
    这里将解析后的文档存储到新建的变量 soup 中
    '''
    def getOnePageData(self, pageNum):
        url = self.base_url + str(pageNum)
        strhtml = requests.get(url, headers=self.headers)  # Get方式获取网页数据
        # 更新refer
        self.headers['referer'] = url
        soup = BeautifulSoup(strhtml.text, 'lxml')
        # 接下来用 select（选择器）定位数据,获取每页的所有公司
        cs = soup.select('#searchlist > table > tbody > tr')
        csInfos = []
        for item in cs:
            # 获取一个公司的信息
            aInfo = self.getOneCompanyData(item)
            if aInfo == False:
                continue
            #去掉‘\n’ ‘ ’
            aInfo['addr'] = self.tripStr(aInfo['addr'])
            aInfo['during'] = self.tripStr(aInfo['during'])
            csInfos.append(aInfo)

        return csInfos



    '''
    获取每一个公司的信息
    company:一个公司的soup
    返回：false不符合要求；result{}公司信息
    '''
    def getOneCompanyData(self, company):
        # 获取第二个和第三个td子节点
        a1 = company.select('td:nth-child(2) > a')[0]
        companyName = a1.get_text()  # 公司名字
        href = a1['href']  # 公司连接
        # 老板名字
        bossName = company.select('td:nth-child(2) > p:nth-child(3) > a')[0].string
        # 成立时间
        # createDate = company.select('td:nth-child(2) > p:nth-child(3) > span:nth-child(3)')[0].string
        # 地址
        addr = company.select('td:nth-child(2) > p:nth-child(5)')[0].string
        # 状态
        status = company.select('td.statustd > span')[0].string
        if status == '存续':
            return False
        '''
         isr = self.isHaveStr(companyName)
            if isr == False:
            return False
        '''
        # 获取其他信息
        otherInfo = self.getCompanyInfo(href)
        '''
        isr = self.isHaveStr(otherInfo['businessScope'])
        if isr == False:
            return False
        '''

        result = {
            'companyName': companyName,
            'bossName': bossName,
            'addr': addr,
            'status': status,
            'during': otherInfo['during'],
            'businessScope': otherInfo['businessScope']
        }

        return result



    '''
    公司主页的信息
    rurl:相对url
    '''
    def getCompanyInfo(self, rurl):
        url = 'https://www.qcc.com' + rurl
        strhtml = requests.get(url, headers=self.headers)  # Get方式获取网页数据
        soup = BeautifulSoup(strhtml.text, 'lxml')
        # 时间
        during = soup.select('#cominfo > div:nth-child(2) > table > tr:nth-child(5) > td:nth-child(4)')[0].string
        # 经营范围
        businessScope = soup.select('#cominfo > div:nth-child(2) > table > tr:nth-child(10) > td:nth-child(2)')[
            0].string
        time.sleep(3)
        return {'during': during, 'businessScope': businessScope}



    '''
    判断字符串s是否包含‘软件’、‘科技’、‘网络’、‘信息’
    '''
    def isHaveStr(self, s):
        if s.find('软件') != -1:
            return True
        if s.find('科技') != -1:
            return True
        if s.find('网络') != -1:
            return True
        if s.find('信息') != -1:
            return True
        return False



    '''
    去掉多余的‘\n’ ' '
    '''
    def tripStr(self, s):
        s = s.replace('\n', '')
        s = s.replace(' ', '')
        return s