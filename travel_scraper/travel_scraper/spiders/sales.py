import scrapy
from scrapy_selenium import SeleniumRequest

class TravelTriangleSpider(scrapy.Spider):
    name = "traveltriangle"
    allowed_domains = ["tourradar.com"]
    start_urls = ["https://www.tourradar.com/deals/india"]

    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.tourradar.com/deals/india",
            callback=self.parse,
            wait_time=3
        )

    def parse(self, response):
        packages = response.css("div.serp-content div.js-serp-tour-list.list div.tourCardContainer")

        if not packages:
            self.logger.warning("No tour packages found. Check if the page is JavaScript-rendered.")

        for package in packages:
            yield {
                "title": package.css("h3.tourCard-title span::text").get(),
                "price": package.css("div.tourCard-price span::text").get(),
                "duration": package.css("div.tourCard-length span::text").get(),
                "link": response.urljoin(package.css("a.tourCard-overlay::attr(href)").get()),
            }

        # Handle pagination
        next_page = response.css("a.pagination-next::attr(href)").get()
        if next_page:
            yield SeleniumRequest(url=response.urljoin(next_page), callback=self.parse, wait_time=5)




