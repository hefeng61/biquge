# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request

from itemadapter import ItemAdapter
import os
from urllib import request

class BiqugePipeline:

    def __init__(self):
        # 查看当前目录，join是拼接构建的是绝对路径
        self.img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '壁纸')
        if not os.path.exists(self.img_path):
            # 如果没有该路径则新建路径
            os.mkdir(self.img_path)

    def process_item(self, item, spider):
        pic_name = item['pic_name']
        pic_url = 'https://bing.ioliu.cn' + item['pic_url'].split('?')[0]
        print('----------download------------')
        print(pic_url)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,zh-TW;q=0.7,en-US;q=0.6,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.176217171.1621396438; Hm_lvt_667639aad0d4654c92786a241a486361=1621396439,1623223373; likes=',
            'Host': 'bing.ioliu.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        urllib.request.Request(url=pic_url, headers=headers)
        request.urlretrieve(pic_url, os.path.join(self.img_path, pic_name + '.jpg'))
