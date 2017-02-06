# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Identity



class BookItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    pub_date = scrapy.Field()
    holding_list = scrapy.Field()

class BookItemLoader(scrapy.loader.ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
    holding_list_in = Identity()
    holding_list_out = Identity()


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    
class NewsItemLoader(scrapy.loader.ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
    
    

            