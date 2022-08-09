import requests
import pandas as pd
import json
import pymysql
from sqlalchemy import create_engine

df = []


# """TASK 1: Pull data from balldontlie.io, 100 members"""
# URL ="https://www.balldontlie.io/api/v1/players"
# PARAMS = {'per_page': 100} #params to pull 100 players
# r = requests.get(url = URL, params = PARAMS) #create http request, needs requests library
# data = r.json()

user = 'root'
hostip = '34.163.182.248'
passwd = 'Ciocanul12%40'
dbname = 'academy'

engine = create_engine('mysql+pymysql://root:Ciocanul12%40@34.163.182.248/academy')
#engine = create_engine('mysql+pymysql://user:passwd@hostip/dbname')

"""GRAB NBA_Players from Database"""
nba_salary = pd.read_sql_query('''SELECT * FROM nba_salary''',con = engine)
nba_savings = pd.read_sql_query('''SELECT * FROM nba_savings''',con = engine)
nba_players = pd.read_sql_query('''SELECT * FROM nba_players''',con = engine)
df = nba_players
df = df.join(nba_salary['Salary'], on='id')
df = df.join(nba_savings['Savings'], on='id')

"""Push into fabian_players table at database academy"""
df.to_sql('fabian_players', con=engine, if_exists= 'replace')






