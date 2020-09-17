import datetime
import json
from datetime import datetime, timezone
import scrapy
import requests
from ..items import DatabaseItem



class DailyrotoCom(scrapy.Spider):
    name = "dailyroto_com"
    start_urls = [r'https://dailyroto.com/nfl-lineup-optimizer/']
    base_url = 'https://dailyroto.com'

    custom_settings = {
        'ITEM_PIPELINES': {'database.pipelines.DatabasePipeline': 300}
    }

    def start_requests(self):
        start_url = f'https://dailyroto.com/OPTO/data/data_all.php?sport=nfl&action=undefined&slateID=undefined'
        yield scrapy.Request(url=start_url, callback=self.parse_nfl)

    def parse_nfl(self, response):
        json_sport = response.json()
        items = DatabaseItem()
        for game in json_sport['Baselines']['Players']:
            items['PlayerID'] = game.get('PlayerID')
            items['Year'] = game.get('Season')
            items['Week'] = game.get('Week')
            items['Team'] = game.get('Team')
            items['Position'] = game.get('Position')
            items['Player'] = game.get('Player')
            items['Opp'] = game.get('Opp')
            items['OppRank'] = game.get('OppRank')
            items['MSPass'] = game.get('MSPass')
            items['PassYards'] = game.get('PassYards')
            items['MSRush'] = game.get('MSRush')
            items['YPC'] = game.get('YPC')
            items['MSRushTD'] = game.get('MSRushTD')
            items['MSTargets'] = game.get('MSTargets')
            items['YPT'] = game.get('YPT')
            items['ReceptionRate'] = game.get('ReceptionRate')
            items['MSRecTD'] = game.get('MSRecTD')
            try:
                items['Salary'] = json_sport.get('Slates')[0].get('Players').get(f'{items["PlayerID"]}').get('Salary')
            except Exception:
                items['Salary'] = None
            items['INTRate'] = game.get('INTRate')
            items['FumbleRate'] = game.get('FumbleRate')
            items['FDProj'] = game.get('FDProj')
            items['DKProj'] = game.get('DKProj')  ### Points
            items['FanDuelSalary'] = game.get('FanDuelSalary')
            items['DraftKingsSalary'] = game.get('DraftKingsSalary')
            items['publicOwnedDK'] = game.get('publicOwnedDK')
            items['publicOwnedFD'] = game.get('publicOwnedFD')
            items['changed'] = game.get('changed')
            items['FDActual'] = game.get('FDActual')
            items['DKActual'] = game.get('DKActual')
            items['YahooActual'] = game.get('YahooActual')
            yield items