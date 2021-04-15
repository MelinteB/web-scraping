# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_whitespace(value):
    return value.strip()


def remove_in_space(value):
    return value.replace('Â','')

def remove_EOL(value):
    return value.replace('\n','')
class ScrapItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace,remove_in_space), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace,remove_EOL), output_processor=TakeFirst())
    location = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace), output_processor=TakeFirst())
    link=scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())