# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ToProductSpider(scrapy.Spider):
    name = "americanas-produto-item"
    start_urls = [ 
       'https://www.americanas.com.br/produto/134186808'
      ]
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    allowed_domains = ['www.americanas.com.br']
    download_delay = 1.5

    def process_float_or_int(value):
        try:
            return eval(value)
        except:
            return value

    def parse(self, response):

               yield {                 
                  'id': response.css('span.TextUI-sc-12tokcy-0.hdQYf::text').extract()[1],       
                  'breadcrumb': response.css('span.TextUI-ohhfq9-5.gomuaV.TextUI-sc-12tokcy-0.bLZSPZ::text').extract(),
                  'name': response.css('.product-title__TitleUI-sc-116vf1e-2.bDZZCj.TitleH1-sc-1wh9e1x-0.kSKgXt::text').extract_first(),
                  'img' : response.css("img::attr(title)").extract(),
                  'seller' : response.css('.seller-00776574000660.TextUI-sc-12tokcy-0.LbEgj::text').extract_first(),
                  'price': response.css('.sales-price.main-offer__SalesPrice-sc-1oo1w8r-1.haZIvY.TextUI-sc-12tokcy-0.bLZSPZ::text').extract_first() 
              }

