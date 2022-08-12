# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# # import pandas as pd

# # Base = declarative_base()
# # engine = create_engine('mysql+pymysql://root:kim8912!@localhost:8083/knj', echo=True) 
# # print(engine.execute("select 1").scalar())

# class Sql:

#     def __init__(self):
#         self.engine = create_engine('mysql+pymysql://root:kim8912!@localhost:8083/knj', echo=True) 

#     def sessionmaker(self):
#         Session = sessionmaker(bind=self.engine)
#         session = Session()
#         return session
    
#     def connection(self):
#         conn = self.engine.connect()
#         return conn
    
#     # def go() :
#     #     sql = """SELECT `YEAR`, sum(`VALUE`) as `VALUE`
#     #     FROM (
#     #         SELECT Concat( WEEK(DATES,1), 'week') AS `YEAR`, CNT as `VALUE`  FROM knjoo_table
#     #     ) A
#     #     GROUP BY `YEAR`
#     #     """ 

#     #     df = pd.read_sql(sql, con=engine)   
#     #     print(df)
        
#     #     return df

import pymysql 

class Sql:
    
    def __init__(self):
        print('init')
        # super().__init__()
        self.conn = pymysql.connect(host='mysql', port = 8083, user='root', password='kim8912!', charset='utf8', db = 'knj') 
        self.curs = self.conn.cursor() 

    def go(self) :
        sql = """SELECT `YEAR`, sum(`VALUE`) as `VALUE`
        FROM (
            SELECT Concat( WEEK(DATES,1), 'week') AS `YEAR`, CNT as `VALUE`  FROM knjoo_table
        ) A
        GROUP BY `YEAR`
        """ 

        # with conn:
        #     with conn.cursor() as cur:
        self.curs.execute(sql)
        result = self.curs.fetchall()
        for data in result:
            print(data)
            return data

