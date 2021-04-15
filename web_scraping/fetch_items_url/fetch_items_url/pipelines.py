# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem



class FetchItemsUrlPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='MySql516823',
            database='scrapy'
        )
        self.curr = self.conn.cursor()
    # def create_connection(self):
    #
    # DATABASES = {
    #
    #     'default': {
    #
    #         'ENGINE': 'django.db.backends.postgresql',
    #
    #         'NAME': 'd44osl2009u94f',
    #
    #         'USER': 'jgbczeipuvchtj',
    #
    #         'PASSWORD': '7cd2913a88627b04c5e707886ebc355dc871d9c84b0d56d902964d7c955b0ef7',
    #
    #         'HOST': 'ec2-54-228-174-49.eu-west-1.compute.amazonaws.com',
    #
    #         'PORT': 5432,
    #
    #     }
    #
    # }


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS web_page_ad""")
        self.curr.execute("""CREATE TABLE web_page_ad(
                                id integer NOT NULL AUTO_INCREMENT,
                                title text,
                                price text,
                                description text,
                                location text,
                                link text,
                                PRIMARY KEY (id)
                          )""")






    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline:" + item['title'])
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO web_page_ad (title,price,description,location,link) VALUES (%s,%s,%s,%s,%s)""", (

            item['title'],
            item['price'],
            item['description'],
            item['location'],
            item['link']
        ))

        self.conn.commit()
    # def store_db(self,item):
    #     title=item['title']
    #     price=item['price']
    #     description=item['description']
    #     location=item['location']
    #     self.curr.execute('INSERT INTO web_page_ad (id,title,description,price,location) VALUES '
    #                       '("'+str(ids)+'","'+str(title)+'","'+str(description)+'","'+str(price)+'","'+str(location)+'")')
    #     self.conn.commit()

    # def _get_guid(self, item):
    #     """Generates an unique identifier for a given item."""
    #     # hash based solely in the url field
    #     return md5(item['url']).hexdigest()

class DuplicatePipeline(object):
    def __init__(self):
        self.ids_seen=set()

    def process_item(self,item,spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found %s" % item)
        else:
            self.ids_seen(item['id'])

            return item