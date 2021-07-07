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
        print(self.img_path)
        if not os.path.exists(self.img_path):
            # 如果没有该路径则新建路径
            os.mkdir(self.img_path)

    def process_item(self, item, spider):
        pic_name = item['pic_name']
        # pic_url = 'https://bing.ioliu.cn' + item['pic_url'].split('?')[0]
        pic_url = 'https://bing.ioliu.cn' + item['pic_url']
        pic_name = pic_name.split('，')[0]
        print(pic_name)
        print('----------download------------')
        print(pic_url)
        opener = request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')]
        request.install_opener(opener)
        request.urlretrieve(pic_url, os.path.join(self.img_path, pic_name + '.jpg'))
