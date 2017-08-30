from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from diplomski.getpullrequest.getpullrequest.spiders.pr_spider import PRSpider
import json
import os


def get_number_lines(arg_pr_url):
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(PRSpider, arg_pr_url=arg_pr_url)
    d.addBoth(lambda _: reactor.stop())
    reactor.run(installSignalHandlers=False)

    with open('data.txt', 'r') as f:
            num_lines = json.load(f)
            os.remove('data.txt')
            print(num_lines)
            return num_lines
