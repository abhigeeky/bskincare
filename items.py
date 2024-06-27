# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class BskincareItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    image_url = Field()
    price = Field()
    url = Field()

