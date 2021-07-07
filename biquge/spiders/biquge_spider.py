import scrapy
from biquge.items import BiqugeItem


class BiqugeSpiderSpider(scrapy.Spider):
    name = 'biquge_spider'
    allowed_domains = ['bing.ioliu.cn']
    start_urls = ['https://bing.ioliu.cn/']

    def parse(self, response):
        img_urls = response.xpath("//a[@class='mark']/@href").getall()
        for url in img_urls:
            url = 'https://bing.ioliu.cn'+url
            yield scrapy.Request(url, callback=self.img)

        next_page_url = response.xpath("//div[@class='page']/a[2]/@href").get()
        yield scrapy.Request(next_page_url,callback=self.parse())

    def img(self, response):
        print('----------img---------------')
        item = BiqugeItem()
        pic_url = response.xpath("//a[@class='ctrl download']/@href").get()

        pic_name = response.xpath("//div[@class='description']/p[1]/text()").get()

        release_date = response.xpath("//div[@class='description']/p[3]/em/text()").get()

        item['pic_url'] = pic_url
        item['pic_name'] = pic_name
        item['release_date'] = release_date
        yield item
