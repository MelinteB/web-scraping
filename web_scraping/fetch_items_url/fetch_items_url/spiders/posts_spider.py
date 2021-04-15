import scrapy
from scrapy.loader import ItemLoader
from fetch_items_url.items import ScrapItem
class PostsSpider(scrapy.Spider):

    name = "posts"

    start_urls = [
        'https://www.publi24.ro/anunturi/imobiliare/'
    ]

    def parse(self, response):
        # for post in response.css('.listing-data'):
        for post in response.css('.listing-data'):
            l = ItemLoader(item=ScrapItem(),selector=post)
            l.add_css('title','div h3 a')
            l.add_css('description','div p')
            l.add_css('price','div strong')
            l.add_css('location','div label.article-location span')
            l.add_css('link',"div h3 a::attr('href')")
            yield l.load_item()
        # for post in response.css('#content'):
        #     l = ItemLoader(item=ScrapItem(), selector=post)
        #     l.add_css('listing-image').attrib['style']
        #     yield l.load_item()
        # if response.css('li.arrow a::attr(href)').get().split('=')[1] == '2':
        if response.css('li.arrow.unavailable a::text').get() == '‹':
            next_page = response.css('li.arrow a::attr(href)').get()
        else:
            next_page = response.css('li.arrow a::attr(href)')[1].get()
        if next_page is not None and response.css('li.arrow a::attr(href)').get().split('=')[1] != '5':
            yield response.follow(next_page, callback=self.parse)
