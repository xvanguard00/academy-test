import requests
import pandas as pd
import json
import pymysql
from sqlalchemy import create_engine

df = pd.read_csv('salariesandsavings_radomirfabian.csv')

engine = create_engine('mysql+pymysql://root:sql@172.17.0.4/academy-ready')

df.to_sql('academy-ready', engine)

print(df.head().to_string())

df2 = pd.read_sql_query('''show tables''', engine)
print(df2)


