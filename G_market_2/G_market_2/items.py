import scrapy


class GMarket2Item(scrapy.Item):

    SORTING = scrapy.Field()

    Name = scrapy.Field()

    Price = scrapy.Field()

    URL = scrapy.Field()