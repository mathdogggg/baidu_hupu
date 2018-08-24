#第一版本，仅实现抓取百度搜索到的“不冷笑话”搜索结果并保存到本地文件中
#第二版本需要对获取到的URL进行过滤，但是百度是重定向的，这个需要考虑
#第三步才是获取虎扑页面的正文动图标题和地址，然后在下载中间件里进行图片的下载

from scrapy.cmdline import execute
execute('scrapy crawl baidu_hupu'.split())

# import requests
# import re
# from pyquery import PyQuery
# r = requests.get('http://www.baidu.com/s?ie=UTF-8&wd=%E4%B8%8D%E5%86%B7%E7%AC%91%E8%AF%9D%20site%3Ahupu.com')
# jpy = PyQuery(r.text)
#
# eqid = re.search(r'eqid = "([0-9]|[a-z])*"',r.text).group()#提取百度页面的eqid

