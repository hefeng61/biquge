# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    pic_name = scrapy.Field()
    pic_url = scrapy.Field()
    release_date = scrapy.Field()