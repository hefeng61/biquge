import scrapy
from biquge.items import BiqugeItem


class BiqugeSpiderSpider(scrapy.Spider):
    name = 'biquge_spider'
    allowed_domains = ['bing.ioliu.cn']
    start_urls = ['https://bing.ioliu.cn/']

    def parse(self, response):
        img_urls = response.xpath("//a[@class='mark']/@href").getall()
        # print(img_urls)
        for url in img_urls:
            url = 'https://bing.ioliu.cn'+url
            print('-------------url----------------')
            print(url)
            yield scrapy.Request(url, callback=self.img)

    def img(self, response):
        print('----------img---------------')
        item = BiqugeItem()
        pic_url = response.xpath("//a[@class='ctrl download']/@href").get()
        print('---------pic_url----------------')
        print(pic_url)
        pic_name = response.xpath("//div[@class='description']/p[1]/text()").get()
        print('---------pic_name----------------')
        print(pic_name)
        release_date = response.xpath("//div[@class='description']/p[3]/em/text()").get()
        print('---------release_date----------------')
        print(release_date)
        item['pic_url'] = pic_url
        item['pic_name'] = pic_name
        item['release_date'] = release_date
        print(item)
        yield item
