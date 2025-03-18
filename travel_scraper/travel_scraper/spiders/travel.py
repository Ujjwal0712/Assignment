import scrapy
import json

class TravelSpider(scrapy.Spider):
    name = "travel"
    allowed_domains = ["theculturetrip.com"]
    start_urls = ["https://theculturetrip.com/asia/india/collections/things-to-do"]

    def parse(self, response):
        # Extract all article links
        article_links = response.css('a[href*="/articles/"]::attr(href)').getall()
        for link in article_links:
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        title = response.css('h1::text').get()
        summary = response.css('meta[name="description"]::attr(content)').get()

        # Extracting all paragraphs from the article
        paragraphs = response.css('article p::text').getall()
        full_article = "\n".join(paragraphs)  # Combine all paragraphs into one text block
        categories = response.css("article h2::text").getall()

        structured_data = {
            "title": title,
            "summary": summary,
            "categories": categories,
            "article": full_article,

        }

        # Save to JSON file
        with open("travel_data.json", "a", encoding="utf-8") as file:
            file.write(json.dumps(structured_data, ensure_ascii=False, indent=4) + ",\n")

        yield structured_data