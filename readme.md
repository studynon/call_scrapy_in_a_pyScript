## Use the Scrapy library to crawl the page url
I re-wrote the reptile program with Scrapy library.
Currently on the Internet search Scrapy most of the use of the command line in the operation, the scrapy as an application.
I want to write the function used in a py script, so write this.

Note: On the basis of the bs4 program is different. Later in the online search, found that Scrapy does not support multi-threaded (multi-threaded is Scrapy own internal optimization, but can not be manually configured, still can run more crawlers), yield \ Request \ callback these together With the efficiency is still very high.
