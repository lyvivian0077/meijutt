import scrapy

from meijutt.items import MovieItem


class Home(scrapy.Spider):
    name = "home"
    main_url = "http://www.meijutt.com"
    start_urls = [
        # main_url + '/1_1______.html',
        # main_url + '/1_2______.html',
        # main_url + '/1_3______.html',
        # main_url + '/1_4______.html',
        main_url + '/1_5______.html'
    ]

    def parse(self, response):
        list = response.xpath("//div[@class='cn_box2']")
        for li in list:
            item = MovieItem()
            item['title'] = li.xpath("./div/div/a/@title").extract_first()
            item['cover'] = li.xpath("./div/div/a/img/@src").extract_first()
            item['link'] = self.main_url + li.xpath("./div/div/a/@href").extract_first()
            yield item

        next_page = response.xpath(
            "//div[@class='list3_cn_box ']/div[@class='page']/a[text()='下一页']/@href").extract_first()
        if (next_page):
            next_page = self.main_url + next_page
            yield scrapy.Request(next_page, callback=self.parse)
