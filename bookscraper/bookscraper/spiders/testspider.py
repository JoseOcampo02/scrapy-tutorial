import scrapy


class TestspiderSpider(scrapy.Spider):
    name = "testspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        print("--------------[ parse start ]------------")

        books = response.css('.product_pod')
        for book in books:
            title = book.css("h3 a::text").get()
            price = book.css(".price_color::text").get()
            print(f"{title} : {price}")

        print("--------------[ parse end ]--------------")
