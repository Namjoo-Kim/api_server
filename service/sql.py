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
import pandas as pd

PORT_INFO = pd.read_csv('../PORT_INFO.csv')
class Sql:
    
    def __init__(self):
        print('init')
        # super().__init__()
        self.conn = pymysql.connect(host=PORT_INFO.host[0], port = PORT_INFO.port[0], user= PORT_INFO.user[0], password=PORT_INFO.password[0], charset='utf8', db = PORT_INFO.db[0]) 
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

