# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatabaseItem(scrapy.Item):
    # define the fields for your item here like:
    PlayerID = scrapy.Field()
    Year = scrapy.Field()
    Week = scrapy.Field()
    Team = scrapy.Field()
    Position = scrapy.Field()
    Player = scrapy.Field()
    Opp = scrapy.Field()
    OppRank = scrapy.Field()
    MSPass = scrapy.Field()
    PassYards = scrapy.Field()
    MSRush = scrapy.Field()
    YPC = scrapy.Field()
    MSRushTD = scrapy.Field()
    MSTargets = scrapy.Field()
    YPT = scrapy.Field()
    ReceptionRate = scrapy.Field()
    MSRecTD = scrapy.Field()
    Salary = scrapy.Field()
    INTRate = scrapy.Field()
    FumbleRate = scrapy.Field()
    FDProj = scrapy.Field()
    DKProj = scrapy.Field()
    FanDuelSalary = scrapy.Field()
    DraftKingsSalary = scrapy.Field()
    publicOwnedDK = scrapy.Field()
    publicOwnedFD = scrapy.Field()
    changed = scrapy.Field()
    FDActual = scrapy.Field()
    DKActual = scrapy.Field()
    YahooActual = scrapy.Field()
    pass