import weibo_spider.spider as sp

config = sp._get_config()
wb = sp.Spider(config)
wb.start()  # 爬取微博信息