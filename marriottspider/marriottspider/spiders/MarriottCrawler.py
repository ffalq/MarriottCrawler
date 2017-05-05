import scrapy
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item
import csv

class MarriotSpider(CrawlSpider):
    name = 'marriott'
    allowed_domains = ['marriott.com']
    start_urls = ['http://www.marriott.com/hotel-search']

    rules = {
        Rule(LinkExtractor(allow=('http:\/\/www\.marriott\.com\/hotel-search\/[A-Za-z\-]+[\.]+hotels+([\.]united-states[\/]|[\/])', ))),
        Rule(LinkExtractor(allow=('http:\/\/www\.marriott\.com\/hotel-search\/[A-Za-z\-]+[\.]+hotels+([\.]united-states[\.]+page+[0-9]+[\/]|[\.]+page+[0-9]+[\/])'))),
        Rule(LinkExtractor(allow=('http:\/\/www\.marriott\.com\/hotels\/travel\/[a-z0-9A-Z\-\.]+[^w]')),callback='parse_item')
    }

    def parse_item(self, response):
        yield {
            'name': response.css("a.t-inherit-styles.analytics-click span::text").extract_first().encode('utf-8'),
            'score': response.css("div.l-rating-normal-outof span::text").extract_first(),
            'url': "www.marriott.com" + response.css("a.t-inherit-styles.analytics-click::attr('href')").extract_first().encode('utf-8'),
            'address': self.createAddress(response.css("a.t-address.is-cursor-pointer.analytics-click span::text").extract()).encode('utf-8'),
            'phone': response.css("span.is-hiddenPhone-Number::text").extract_first(),
            'number ratings': self.createRatings(response.css("div.l-float-left.l-margin-left-quarter span::text").re("\d+"))
        }

    def createAddress(self,input_list):
        s=""
        for item in input_list:
            s += str(item) + ','
        return s

    def createRatings(self,input_review):
        if len(input_review) >= 1:
            return input_review[0]
        return ""
