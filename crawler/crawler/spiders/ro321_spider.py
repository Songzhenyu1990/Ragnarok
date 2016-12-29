import scrapy
from crawler.items import RO321Item

class ro321Spider(scrapy.Spider):
    name = "ro321"
    allowed_domain = "ro321.com"
    url_samples = "http://ro321.com/index.php?page=re_item_db&item_id=511"



    def parse(self, response):
        xpath = "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/center/table[2]/tbody"
