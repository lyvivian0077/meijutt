# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class RankItem(scrapy.Item):
    # define the fields for your item here like:
    rank = Field()
    title = Field()
    average_big = Field()
    average_small = Field()
    link = Field()


class MovieItem(scrapy.Item):
    title = Field()
    cover = Field()
    link = Field()
