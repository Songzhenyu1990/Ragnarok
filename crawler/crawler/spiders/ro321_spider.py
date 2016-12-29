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
            item["id"] = sel.xpath('tr[1]/td/table/tr/td[2]/text()').extract()
            item["type"] = sel.xpath('tr[2]/td[1]/text()').extract()
            item["series"] = sel.xpath('tr[2]/td[2]/text()').extract()
            item["buy_price"] = sel.xpath('tr[2]/td[3]/text()').extract()
            item["sell_price"] = sel.xpath('tr[2]/td[4]/text()').extract()
            item["weight"] = sel.xpath('tr[2]/td[5]/text()').extract()
            item["description"] = sel.xpath('tr[3]/td/text()').extract()
            item["script"] = sel.xpath('tr[4]/td/div/text()').extract()
            item["loot"] = (sel.xpath('tr[5]/td/table/tr/td/a/text()').extract(), sel.xpath('tr[5]/td/table/tr/td/a/div/text()').extract())
            item["other_loot"] = sel.xpath('tr[6]/td/a/text()').extract()



            yield item