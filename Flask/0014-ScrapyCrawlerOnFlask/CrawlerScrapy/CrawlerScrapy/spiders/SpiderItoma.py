'''import scrapy


class SpideritomaSpider(scrapy.Spider):
    name = "SpiderItoma"
    allowed_domains = ["itoma.co.uk"]
    start_urls = ["http://itoma.co.uk/"]

    def parse(self, response):
        pass'''
    
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = "SpiderItoma"
    allowed_domains = ["itoma.co.uk"]
    start_urls = ["http://itoma.co.uk/"]
    
    visited_urls = set()
    
    rules = (
        Rule(LinkExtractor(allow_domains=allowed_domains, deny=('elementor', 'cdn', '#', 'privacy-policy')), 
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # extract links to pages on the same domain
        for link in LinkExtractor(allow_domains=self.allowed_domains, 
                                  deny=('elementor', 'cdn', '#', 'privacy-policy')).extract_links(response):
            url = link.url
            if url not in self.visited_urls:
                self.visited_urls.add(url)
                yield {'url': url}

