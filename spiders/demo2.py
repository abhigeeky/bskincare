from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bskincare.items import BskincareItem  # Ensure the import path matches your project structure
import logging

class BskincareScraper(CrawlSpider):
    name = "Bskincareitemscraper"
    allowed_domains = ["bskincaretx.com"]
    start_urls = ["https://www.bskincaretx.com/shop"]

    rules = (
        Rule(LinkExtractor(restrict_css="a.AJctir.bGFTjD.SlYjm7"), callback="parse_item", follow=True),
    )
    def parse_item(self, response):
        item = BskincareItem()
        # Update these selectors based on the actual HTML structure
        title = response.css('h1[data-hook="product-title"]::text').get()
        if title:
            item["title"] = title.strip()
        else:
            logging.error(f"Title not found for URL: {response.url}")
        
        image_url = response.css('img::attr(src)').get()
        if image_url:
            item["image_url"] = response.urljoin(image_url)
        else:
            logging.error(f"Image URL not found for URL: {response.url}")

        # Using the specific selector seen in the HTML structure for price
        price = response.css('span[data-hook="product-item-price-to-pay"]::text').get()
        if not price:
            # Try another selector or method if the first one fails
            price = response.css('span[data-hook="product-item-price-to-pay"]::attr(data-wix-price)').get()
        if price:
            item["price"] = price.strip()
        else:
            logging.error(f"Price not found for URL: {response.url}")

        item["url"] = response.url

        yield item


# scrapy crawl bskincare -o products.json
