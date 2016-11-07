from scrapy.http import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
import logging
import time


class joomler(Spider):
    name = "scrapy"
    allowed_domains = ["chinaz.com"]
    start_urls = ["http://top.chinaz.com/all/index.html"]
    

    def parse(self, response):
        global fw
        print "Working... "+response.url
        sel = Selector(response)
        spans = sel.xpath('//span[@class="col-gray"]')
        items = spans.xpath('text()').extract()
        for item in items[1:]:
            fw.write('%s\n' % item.encode('utf-8'))

        base_urls = "http://top.chinaz.com/all/index_"
        for i in range(2,500):
            url = (base_urls+str(i) + '.html')
            print url
            yield Request(url, callback=self.suppose_to_parse)

        print 'all done!'


    def suppose_to_parse(self, response):
        print "asdasd"
        print response.url
        sel = Selector(response)
        spans = sel.xpath('//span[@class="col-gray"]')
        items = spans.xpath('text()').extract()
        for item in items[1:]:
            fw.write('%s\n' % item.encode('utf-8'))

if __name__ == "__main__":
    time1 = time.time()
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    logging.getLogger('scrapy').setLevel(logging.WARNING)
    filename = 'chinazcom.txt'
    fw = open(filename, 'w')
    process.crawl(joomler)
    process.start() # the script will block here until the crawling is finished
    fw.close()
    time2 = time.time()
    print time2-time1
