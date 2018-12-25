# -*- coding: utf-8 -*-
import scrapy
import json

class SpoodySpider(scrapy.Spider):
    name = 'spoody'
    allowed_domains = ['www.citilink.ru']
    start_urls = ['http://www.citilink.ru/catalog/mobile/cell_phones/?available=1']
    #start_urls = ['https://www.citilink.ru/catalog/audio_and_digits/tv/?available=1']

    def __init__(self, *args, **kwargs):
    	self.current_page = 1
    	self.last_page = 17
        super(SpoodySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        class_name = 'js--subcategory-product-item subcategory-product-item product_data__gtm-js  product_data__pageevents-js ddl_product'
        for data_params in response.xpath('//div[@class="{}"]/@data-params'.format(class_name)):
            p = json.loads(data_params.extract())
            yield {
                'price': int(p['price']),
            }

        self.current_page += 1
        if self.current_page > self.last_page:
            return

        urlbase = '/'.join(response.url.split('/')[:-1])
        next_page_url = '{}/?available=1&p={}'.format(urlbase, self.current_page)
        yield scrapy.Request(response.urljoin(next_page_url))
