# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderPipeline:
    def process_item(self, item, spider):
        titles = item['titles']
        types = item['types']
        dates = item['dates']
        line = f'{titles},{types},{dates}\n'
        with open('./maoyan_scrapy.csv', 'a+', encoding='utf-8') as fp:
            fp.write(line)
        return item

