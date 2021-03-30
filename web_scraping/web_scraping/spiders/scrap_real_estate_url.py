import scrapy

class ScrapSpider(scrapy.Spider):
    name='scrap'

    start_urls=[
        'https://www.publi24.ro/anunturi/imobiliare/de-vanzare/apartamente/'
    ]

    def parse(self,response):
        for scrap in response.xpath("//div[@id='content']"):
            yield {
                'scrap_text' : scrap.xpath(".//div[@id='content']/div/div/div/ul/li/div/div/h3/a").extract_first()
            }
        next_page=response.xpath("//div[@id='content']/div/div/div/ul/li[@class='arrow']/a").extract_first()
        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)
