import scrapy


class FinanceItem(scrapy.Item):

    Name = scrapy.Field()
    
    Date = scrapy.Field()

    매출액 = scrapy.Field()

    영업이익 = scrapy.Field()

    당기순이익 = scrapy.Field()

    ROE = scrapy.Field()

    PER = scrapy.Field()

    PBR = scrapy.Field()



