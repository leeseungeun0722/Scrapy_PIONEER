import scrapy
from G_market_2.items import GMarket2Item

KEYWORD = input('찾고 싶은 키워드를 입력해주세요 (키워드는 띄어쓰기로 구분 됩니다) : ').split(' ')

while True:

    TYPE = input('원하는 정렬을 선택해주세요... 판매 인기순 (8) 낮은 가격순 (1) 높은 가격순 (2) 상품평이 많은순 (13) 신규상품순 (3) : ')

    if TYPE == '8' or TYPE == '1' or TYPE == '2' or TYPE == '13' or TYPE == '3':

        break

if TYPE == '8':

    SORTING = '판매 인기순 정렬'


if TYPE == '1':
    
    SORTING = '판매 인기순 정렬'

if TYPE == '2':
    
    SORTING = '판매 인기순 정렬'

if TYPE == '13':
    
    SORTING = '판매 인기순 정렬'

if TYPE == '3':
    
    SORTING = '판매 인기순 정렬'

INPUTKEY = '+'.join(KEYWORD)

#지마켓 사이트에서 무료배송만 눌렀을시 URL 변동 => &f=d:f
URL = 'https://browse.gmarket.co.kr/search?keyword=' + INPUTKEY + '&f=d:f&s=' + TYPE

class GmarketSpider(scrapy.Spider):
    #Spider 이름
    name = 'spider'

    #크롤링을 진행하게 될 사이트 URL
    start_urls = [URL]

    def parse(self, response):
        
        #전역변수 설정
        global url
        
        #세부상품 URL 추출
        for i in range(1,101):

            # 세부사이트 URL
            URL = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]/div[1]/div[2]/div[1]/div[2]/span/a')
            
            div = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]')

            #URL이 빈칸이 아니라면 span 앞이 div[2]이다
            if (URL != []):
                
                href = div.xpath('./div[1]/div[2]/div[1]/div[2]/span/a/@href')

                url = response.urljoin(href[0].extract())
    
                yield scrapy.Request(url, callback = self.parse_page_content1)
            
            #URL이 빈칸이라면 span 앞이 div[1]이다
            if(URL == []):

                href = div.xpath('./div[1]/div[2]/div[1]/div[1]/span/a/@href')
                
                url = response.urljoin(href[0].extract())
                
                yield scrapy.Request(url, callback = self.parse_page_content2)

    
    def parse_page_content1(self, response):
        
        #item 호출
        item = GMarket2Item()

        item['SORTING'] = SORTING

        item['Name'] = response.xpath('//*[@id="itemcase_basic"]/div/h1/text()')[0].extract()
            
        item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
            
        item['URL'] = url 

        return item

    def parse_page_content2(self, response):

        item = GMarket2Item()

        item['SORTING'] = SORTING

        item['Name'] = response.xpath('//*[@id="itemcase_basic"]/div/h1/text()')[0].extract()
            
        item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
            
        item['URL'] = url 

        return item






