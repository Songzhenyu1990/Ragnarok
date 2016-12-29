import scrapy
from crawler.items import RO321Item

class Ro321Spider(scrapy.Spider):
    name = "ro321"
    allowed_domain = "ro321.com"
    url_sample = "http://ro321.com/index.php?page=re_item_db&item_id=511"
    start_urls = [url_sample]

    def parse(self, response):
        xpath = "/html/body/table/tr[2]/td/table/tr[2]/td[2]/table/tr[2]/td[2]/center/table[2]"
        for sel in response.xpath(xpath):
            item = RO321Item()
            item["name"] = sel.xpath('tr[1]/td/table/tr/td[2]/b/text()').extract()
            yield item