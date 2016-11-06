# -*- coding:utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector 
from scrapy.crawler import CrawlerProcess
import logging

def create_myspider(nm, dmn, url):
	class MySpider(Spider):
	    # Your spider definition
	    name = nm#"scrp"  
	    allowed_domains = dmn#["baidu.com"]  
	    start_urls = [  
	        url#"http://tieba.baidu.com/"  
	    ]  
	  
	    def parse(self, response):  
	    	items = []
	    	sel = Selector(response)
	    	spans = sel.xpath('//span[@class="col-gray"]')
	    	filename = response.url.split("/")[2] 
	    	fw = open(filename, 'w')
	    	items = spans.xpath('text()').extract()
	    	for item in items[1:]:
	    		fw.write('%s\n' % item.encode('utf-8'))
	        fw.close()
	return MySpider

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    logging.getLogger('scrapy').setLevel(logging.WARNING)
    myspider = create_myspider('scrp','chinaz.com','http://top.chinaz.com/all/index_2.html')
    process.crawl(myspider)
    process.start() # the script will block here until the crawling is finished


