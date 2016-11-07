from scrapy.http import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
import logging


class joomler(Spider):
    name = "scrapy"
    allowed_domains = ["chinaz.com"]
    start_urls = ["http://top.chinaz.com/all/index.html"]

    def parse(self, response):
        global fw
        global url_count
        print "Working... "+response.url
        sel = Selector(response)
        spans = sel.xpath('//span[@class="col-gray"]')
        items = spans.xpath('text()').extract()
        for item in items[1:]:
            fw.write('%s\n' % item.encode('utf-8'))
        urls = sel.xpath('//div[@class="ListPageWrap"]/a/@href').extract()
        url = 'http://top.chinaz.com/all/'+urls[-1]
        url_count += 1
        if url_count < 20:
            yield Request(url, callback=self.parse)

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    logging.getLogger('scrapy').setLevel(logging.WARNING)
    filename = 'chinazcom.txt'
    fw = open(filename, 'w')
    url_count = 0
    process.crawl(joomler)
    process.start() # the script will block here until the crawling is finished
    fw.close()
