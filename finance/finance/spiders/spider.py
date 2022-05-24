import scrapy
import requests
from finance.items import FinanceItem

Finance = []

#동적 웹페이지라 request함수로 API를 직접 호출 후 text로 변경
F_URL = requests.get('https://finance.naver.com/sise/sise_quant.naver?sosok=0').text

string = F_URL

# /item/main.naver?code= 글자를 추출하기 위함
string = string.replace('\n',"")
string = string.replace('\t',"")
strings = string.split('"')

for main in strings:
    
    if '/item/main.naver?code=' in main :

        #재무재표를 추출하기 위한 각각의 주식명 추출
        Finance.append(main)

class SpiderSpider(scrapy.Spider):

    name = 'spider'

    start_urls = ['http://finance.naver.com/']

    def parse(self,response):

        for url in Finance:
    
            URL = 'http://finance.naver.com' + url

            yield scrapy.Request(URL, callback=self.parse_page_contents)
    
    def parse_page_contents(self,response):
        
        item = FinanceItem()
        매출액_List = []
        영업이익_List = []
        Date_List = []
        당기순이익_List = []
        ROE_List = []
        PER_List = []
        PBR_List = []

        # 재무재표 추출
        for i in range(1,11):

            Name = response.xpath('//*[@id="middle"]/div[1]/div[1]/h2/a/text()')[0].extract().strip()
            Date = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/thead/tr[2]/th[{i}]/text()')[0].extract().strip()
            Date_List.append(Date)
            매출액_Str =  str(response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[1]/td[{i}]'))
            영업이익_Str = str(response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[2]/td[{i}]'))
            당기순이익_Str = str(response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[3]/td[{i}]'))
            ROE_Str = str(response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[{i}]'))
            PER_Str = str(response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[{i}]'))
            PBR_Str = str(response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[13]/td[{i}]'))

            # null일 경우 null이 아닐경우 분류
            if 'null' not in 매출액_Str :
                매출액 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[1]/td[{i}]/text()')[0].extract().strip()
                if 매출액 == '' :
                    매출액 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[1]/td[{i}]/em/text()')[0].extract().strip()
                    매출액_List.append(매출액)
                else :
                    매출액_List.append(매출액)
            else :
                매출액 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[1]/td[{i}]/text()')[0].extract().strip()
                매출액_List.append(매출액)

            if 'null' not in 영업이익_Str :
                영업이익 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[2]/td[{i}]/text()')[0].extract().strip()   
                if 영업이익 == '' :
                    영업이익 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[2]/td[{i}]/em/text()')[0].extract().strip()
                    영업이익_List.append(영업이익)
                else :
                    영업이익_List.append(영업이익) 
            else :
                영업이익 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[2]/td[{i}]/text()')[0].extract().strip()   
                영업이익_List.append(영업이익)

            if 'null' not in 당기순이익_Str :
                당기순이익 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[3]/td[{i}]/text()')[0].extract().strip()  
                if 당기순이익 == '' :
                    당기순이익 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[3]/td[{i}]/em/text()')[0].extract().strip()  
                    당기순이익_List.append(당기순이익)
                else :
                    당기순이익_List.append(당기순이익)              
            else :
                당기순이익 = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[3]/td[{i}]/text()')[0].extract().strip()  
                당기순이익_List.append(당기순이익)

            if 'null' not in ROE_Str :
                ROE = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[{i}]/text()')[0].extract().strip()  
                if ROE == '' :
                    ROE = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[{i}]/em/text()')[0].extract().strip()  
                    ROE_List.append(ROE)      
                else :
                    ROE_List.append(ROE)          
            else :
                ROE = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[6]/td[{i}]/text()')[0].extract().strip()  
                ROE_List.append(ROE)

            if 'null' not in PER_Str :
                PER = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[{i}]/text()')[0].extract().strip()  
                if PER == '' :
                    PER = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[{i}]/em/text()')[0].extract().strip()   
                    PER_List.append(PER)
                else :
                    PER_List.append(PER)          
            else :
                PER = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[11]/td[{i}]/text()')[0].extract().strip()  
                PER_List.append(PER)

            if 'null' not in PBR_Str :
                PBR = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[13]/td[{i}]/text()')[0].extract().strip()  
                if PBR == '' :
                    PBR = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[13]/td[{i}]/em/text()')[0].extract().strip()  
                    PBR_List.append(PBR)
                else :
                    PBR_List.append(PBR)          
            else :
                PBR = response.xpath(f'//*[@id="content"]/div[4]/div[1]/table/tbody/tr[13]/td[{i}]/text()')[0].extract().strip()  
                PBR_List.append(PBR)

        # 재무재표 item 저장
        item['Name'] = Name
        item['매출액'] = 매출액_List
        item['영업이익'] = 영업이익_List
        item['Date'] = Date_List
        item['당기순이익'] = 당기순이익_List
        item['ROE'] = ROE_List
        item['PER'] = PER_List
        item['PBR'] = PBR_List

        return item
        


        