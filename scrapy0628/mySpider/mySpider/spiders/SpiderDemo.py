import scrapy


class SpiderDemo(scrapy.Spider):
    name = 'myspider'

    # 'https://top.baidu.com/board?tab=realtime'
   
    start_urls = [
            'https://tophub.today/'
            ]
        
    def parse(self, response):
        
        for h in response.xpath('//div[@class="cc-cd-lb"]/span/text()').getall():
            yield {'title': h}