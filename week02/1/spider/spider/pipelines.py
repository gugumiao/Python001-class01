# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class SpiderPipeline:

    def __init__(self):
        self.host = '116.63.131.185'
        self.port = 6033
        self.user = 'geektime'
        self.password = 'python3'


    def open_spider(self, spider):
        # print('open')
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, charset='utf8')
        self.cur = self.conn.cursor()
        self.cur.execute('use geektime;')
        query = 'create table if not exists `movie` (`id` int(11) auto_increment, `title` varchar(100) not null, `type` varchar(20) not null, `date` varchar(20) not null, primary key(`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'
        self.cur.execute(query)
        self.conn.commit()


    def close_spider(self, spider):
        # print('close')
        self.conn.close()


    def process_item(self, item, spider):
        # print('process_item')
        query = f'insert into `movie` (`title`, `type`, `date`) values ("{item["titles"]}", "{item["types"]}", "{item["dates"]}")'
        self.cur.execute(query)
        self.conn.commit()
        return item

