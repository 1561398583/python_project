import time
import qccObj

num = 0

f = open('E:\\python_work\\find_company\\notExist', "a")

for x in range(1, 1001):
    try:
        cookie = "UM_distinctid=17a70797b303b0-0929cb8a9f5b67-6373267-100200-17a70797b31596; QCCSESSID=amkv8kae564sompbb1hs1jf6q5; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201627274378801%2C%22updated%22%3A%201627274400200%2C%22info%22%3A%201627274378806%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E4%BC%81%E6%9F%A5%E6%9F%A5%E7%BD%91%E7%AB%99%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.google.com.hk%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%22undefined%22%7D; CNZZDATA1254842228=1909718359-1625381967-https%253A%252F%252Fwww.google.com.hk%252F%7C1629444050; acw_tc=744d4a0f16294490796105115eeee9b2304cd93cea289ef679977526c7; zg_did=%7B%22did%22%3A%20%2217a707985611de-0e7ad50ae1b1e6-6373267-100200-17a707985622bf%22%7D; zg_294c2ba1ecc244809c552f8f6fd2a440=%7B%22sid%22%3A%201629446975194%2C%22updated%22%3A%201629449080123%2C%22info%22%3A%201628928664970%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22cuid%22%3A%20%22undefined%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201629446975194%7D"

        qcc = qccObj.QCC(cookie)
        r = qcc.getOnePageData(x)
        print('page ' + str(x) + ' get ' + str(len(r)) + "\n")
        num += len(r)
        for item in r:
            s = 'companyName: ' + item['companyName'] + ', bossName: ' + item['bossName'] + ', addr: ' + item[
                'addr'] + ', status: ' + item['status'] + ', during: ' + item['during'] + ', businessScope: ' + item[
                    'businessScope'] + "\n"
            f.write(s)
    except Exception as err:
        print(str(err))
    time.sleep(3)

f.close()
print('finish total get  ' + str(num))
