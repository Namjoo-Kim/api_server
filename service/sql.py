import pymysql 
import os
from dotenv import load_dotenv
import json

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))
load_dotenv()

class Sql:
    
    def __init__(self):
        print('init')
        # super().__init__()
        self.conn = pymysql.connect(host=os.environ["host"], port = int(os.environ["port"]), user= os.environ["user"], password=os.environ["password"], charset='utf8', db = os.environ["db"]) 
        self.curs = self.conn.cursor() 

    def go(self, item_id) :
        
        if item_id == '2' :
            sql = """SELECT `YEAR` as `year`, sum(`VALUE`) as `value`
            FROM (
                SELECT Concat( YEAR(DATES), 'Y') AS `YEAR`, CNT as `VALUE`  FROM knjoo_table
            ) A
            GROUP BY `YEAR`
            """ 
        elif item_id == '3' :
            sql = """SELECT `YEAR` as `year`, sum(`VALUE`) as `value`
            FROM (
                SELECT Concat( QUARTER(DATES), 'Q') AS `YEAR`, CNT as `VALUE`  FROM knjoo_table
            ) A
            GROUP BY `YEAR`
            """ 
        else :
            sql = """SELECT `YEAR` as `year`, sum(`VALUE`) as `value`
            FROM (
                SELECT Concat( WEEK(DATES,1), 'week') AS `YEAR`, CNT as `VALUE`  FROM knjoo_table
            ) A
            GROUP BY `YEAR`
            """ 
            
        # with conn:
        #     with conn.cursor() as cur:
        self.curs.execute(sql)
        
        results = [dict((self.curs.description[i][0], value) for i, value in enumerate(row)) for row in self.curs.fetchall()]
        print(results)
        
        return results
        
        # results = self.curs.fetchall()
        # print(results)
        # data = json.dumps(results)
        # print(data)
        # return data
        
        
        # results = self.curs.fetchall()
        # for result in results:
        #     print(result)
        #     return result

