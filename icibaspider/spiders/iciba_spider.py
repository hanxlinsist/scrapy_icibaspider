import scrapy
from icibaspider.items import IcibaspiderItem 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

class IcibaSpider(CrawlSpider):
    name = 'iciba'
    allowed_domains = ['iciba.com']
    start_urls = ['http://news.iciba.com/dailysentence/history.html']

    rules = [
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(sle(allow=("/appv3/wwwroot/ds.php\?action=history&ob=1&order=2&page=\d+#nav", )), follow=True),


        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(sle(allow=("/dailysentence/detail-\d+.html#nav")), callback='parse_item'),
    ]

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = IcibaspiderItem()
        item['en'] = response.xpath("//li[@class='en']/descendant::text()").extract()
        item['cn'] = response.xpath("//li[@class='cn']/descendant::text()").extract()
        item['url'] = response.url

        return item
