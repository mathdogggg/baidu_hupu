# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import BaiduItem
import re
from scrapy.http import Request #用于构造抓取详情页请求
class BaiduHupuSpider(scrapy.Spider):
    name = 'baidu_hupu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=%E4%B8%8D%E5%86%B7%E7%AC%91%E8%AF%9D&pn=0&oq=%E4%B8%8D%E5%86%B7%E7%AC%91%E8%AF%9D&ct=2097152&ie=utf-8&si=hupu.com&rsv_pq=ad6601de000147ef&rsv_t=1740okrVICj%2BZzmaAuhUfBVVYyzlxA%2FUBkTpHHnAYYdNIh5HTkdxK0T4dRE']

    def parse(self, response):
        jpy = PyQuery(response.text)
        title_list = jpy('#content_left > div >h3 > a').items()
        eqid = re.search(r'eqid = "([0-9]|[a-z])*"',response.text).group()
        eqid2 =eqid.split(r'"')[-2] # 获取搜索页面的eqid，搜索链接没这个eqid无法跳转
        for it in title_list:
            if it.text().startswith("《不冷笑话》"): # 判断开头是否是以《不冷笑话》开始，排除一些不相关搜索项
                item = BaiduItem()
                item['name'] = it.text()
                item['url'] = it.attr('href')+'&eqid='+eqid2

                # 发送抓取详情页请求
                if item['url']:
                    yield Request(
                        item['url'],
                        callback=self.detail_parse,
                        meta={'item': item},
                        priority=10,
                        dont_filter=True
                    )
                # yield item
        next_page = jpy('#page > a:nth-last-child(1)').attr('href')

        # 翻页功能
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page,callback=self.parse)
        #     print('url is %s' % next_page)


    #抓取详情页，未完工
    def detail_parse(self,response):
        if re.match(r'https://bbs.hupu.com/[0-9]*.html',response.url): # 排除分页链接，只取第一页的数据
            jpy = PyQuery(response.text)
            item = response.meta['item']
            title = jpy(r'#j_data').text()
            item['title'] = title
            return item