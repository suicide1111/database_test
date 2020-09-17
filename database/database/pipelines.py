# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from database.items import DatabaseItem

hostname = 'localhost'  # mysql server
username = 'root'  # user name
password = ''  # user password
dbname = 'test'  # dbname


class DatabasePipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host=hostname,
            user=username,
            passwd=password,
        )
        self.curr = self.conn.cursor()
        self.curr.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
        self.curr.execute(f"USE {dbname}")

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS dailyroto_nfl_projections(
                        PlayerID INT,
                        Year INT,
                        Week INT,
                        Team VARCHAR(64),
                        Position VARCHAR(64),
                        Player VARCHAR(64),
                        Opp VARCHAR(64),
                        OppRank FLOAT,
                        MSPass FLOAT,
                        PassYards FLOAT,
                        MSRush FLOAT,
                        YPC FLOAT,
                        MSRushTD FLOAT,
                        MSTargets FLOAT,
                        YPT FLOAT,
                        ReceptionRate FLOAT,
                        MSRecTD FLOAT,
                        Salary FLOAT,
                        INTRate FLOAT,
                        FumbleRate FLOAT,
                        FDProj FLOAT,
                        DKProj FLOAT,
                        FanDuelSalary VARCHAR(64),
                        DraftKingsSalary VARCHAR(64),
                        publicOwnedDK FLOAT,
                        publicOwnedFD FLOAT,
                        changed FLOAT,
                        FDActual FLOAT,
                        DKActual FLOAT,
                        YahooActual FLOAT,
                        timestamp VARCHAR(128),
                        PRIMARY KEY (PlayerID, Week, Year, timestamp)
                        )""")

    def process_item(self, item, spider):
        if isinstance(item, DatabaseItem):
            self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(
            """insert into dailyroto_nfl_projections values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp(6))""",
            (
                item['PlayerID'],
                item['Year'],
                item['Week'],
                item['Team'],
                item['Position'],
                item['Player'],
                item['Opp'],
                item['OppRank'],
                item['MSPass'],
                item['PassYards'],
                item['MSRush'],
                item['YPC'],
                item['MSRushTD'],
                item['MSTargets'],
                item['YPT'],
                item['ReceptionRate'],
                item['MSRecTD'],
                item['Salary'],
                item['INTRate'],
                item['FumbleRate'],
                item['FDProj'],
                item['DKProj'],
                item['FanDuelSalary'],
                item['DraftKingsSalary'],
                item['publicOwnedDK'],
                item['publicOwnedFD'],
                item['changed'],
                item['FDActual'],
                item['DKActual'],
                item['YahooActual'],
            ))
        self.conn.commit()

