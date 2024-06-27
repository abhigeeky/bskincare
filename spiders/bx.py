import scrapy

class BxSpider(scrapy.Spider):
    name = "bx"
    allowed_domains = ["www.bskincaretx.com"]
    start_urls = ["https://www.bskincaretx.com/shop"]

    def parse(self, response):
        for item in response.css('div.swiper-slide'):
            title = item.css('p::text').getall()[0]
            url = item.css('a::attr(href)').get()
            price = item.css('span::text').getall()[1]
        
            yield response.follow(url, callback=self.parse_product, meta={'title': title, 'url': url, 'price': price})

    def parse_product(self, response):
        title = response.meta['title']
        url = response.meta['url']
        price = response.meta['price']
        description = response.css('pre p::text').getall()
    
        yield{
            "title": title,
            "url": url,
            "price": price,
            "description": description
        }

    # def parse(self, response):
    #     for item in response.css('div.swiper-slide'):

    #         yield{
    #             "title":item.css('p::text').getall() [0],
    #             "url": item.css('a::attr(href)').get(),
    #             "Price": item.css('span::text').getall() [1]
    #         }
    #     # next_page = response.css("url").getall()
    #     # print(next_page)
    #     # if next_page is not None:
    #     #     yield response.follow_all(next_page, callback=self.parse)
    #         # pages = item.css('a::attr(href)').get()
    #         # if pages is not None:
    #         #     yield response.follow(pages, callback=self.parse)
            
    #     # for a in response.css("div.swiper-slide a::attr(href)"):
    #     #     yield response.follow(a, callback=self.parse_product)
        
    #     yield from response.follow_all(css="div.swiper-slide a::attr(href)", callback=self.parse_product)

    # def parse_product(self, response):
    #     yield{
    #         "title": response.css('h1::text').get(),
    #         "description": response.css('pre p::text').getall()
    #     }
        