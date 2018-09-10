import scrapy

from meijutt.items import RankItem


class Rank(scrapy.Spider):
    name = "rank"
    main_url = "http://www.meijutt.com"
    start_urls = ['http://www.meijutt.com/alltop_hit.html']

    def parse(self, response):
        top_min = response.xpath("//div[@class='top-min']")
        for top_type in top_min:
            type = top_type.xpath(".//h5/text()").extract_first()
            print(type)
            list = top_type.xpath(".//li")
            items = []
            for li in list:
                rank = li.xpath("./div/i/text()").extract_first()
                title = li.xpath("./h5/a/@title").extract_first()
                average_big = li.xpath("./div/strong/text()").extract_first()
                average_small = li.xpath("./div/span/text()").extract_first()
                link = self.main_url + li.xpath("./h5/a/@href").extract_first()
                print(rank, title, average_big + average_small, link)
                item = RankItem()
                item['rank'] = rank
                item['title'] = title
                item['average_big'] = average_big;
                item['average_small'] = average_small
                item['link'] = link
                items.append(item)
            dict = {'type': type, "items": items}
            yield dict

    def parse_item(self, item):
        pass
