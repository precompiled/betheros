import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst, Compose
import re
import json


class PRSpider(scrapy.Spider):
    name = 'pr_spider'
    start_urls = ['https://bitbucket.org/Di-Mi/eth_hack/pull-requests']
    xpath_added = '//span[@class="lines-added"]/text()'

    def __init__(self, arg_pr_url):
        self.pr_url = arg_pr_url
        self.num_lines = 0
        self.start_urls += f"{arg_pr_url}/ful/diff?_pjax=%23pr-tab-content"
        super().__init__()

    def parse(self, response):
        # page_url = 'https://bitbucket.org/Di-Mi/eth_hack/pull-requests/4/ful/diff?_pjax=%23pr-tab-content'
        page_url = "https://bitbucket.org/Di-Mi/eth_hack/pull-requests/{}/ful/diff?_pjax=%23pr-tab-content".format(self.pr_url)
        return scrapy.Request(page_url,
                             method='GET',
                             body='{"filters": []}',
                             headers={'X-Requested-With': 'XMLHttpRequest',
                                      'Content-Type': 'application/x-www-form-urlencoded'},
                             callback=self.parse2)

    def parse2(self, response):
        for item in response.xpath(self.xpath_added).extract():
            a = re.sub(r'[^\d]+', '', item)
            # print(a)
            self.num_lines += int(a)
        print("number of items = {}".format(self.num_lines))

        with open('data.txt', 'w') as f:
            json.dump(self.num_lines, f)

        return

