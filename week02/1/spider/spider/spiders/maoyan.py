import scrapy
from spider.items import SpiderItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    def requests(self):
        try:
            yield scrapy.Requests(url=start_urls, callback=self.parse)
        except Exception as e:
            print(e)


    def parse(self, response):
        try:
            movie = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
            for m in movie[:10]:
                item = SpiderItem()
                url = m.xpath('./a/@href').extract_first().strip()
                link = 'https://maoyan.com' + url
                item['link'] = link
                yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
        except Exception as e:
            print(e)


    def parse2(self, response):
        try:
            movie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
            item = response.meta['item']
            titles = movie.xpath('./h1/text()').extract_first().strip()
            item['titles'] = titles
            types = movie.xpath('./ul/li[1]/*/text()').extract()
            types = [t.strip() for t in types]
            item['types'] = '/'.join(types)
            dates = movie.xpath('./ul/li[3]/text()').extract_first().strip()
            item['dates'] = dates[:10]
            yield item
        except Exception as e:
            print(e)

