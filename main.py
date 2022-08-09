import re

import requests
import pandas as pd
import json
import pymysql
from sqlalchemy import create_engine

df = []


"""TASK 1: Pull data from balldontlie.io, 100 members"""
URL ="https://www.balldontlie.io/api/v1/players"
PARAMS = {'per_page': 100} #params to pull 100 players
r = requests.get(url = URL, params = PARAMS) #create http request, needs requests library
data = r.json()

jsondata = pd.json_normalize(data, sep=' , ',max_level=3)
datafromsite = pd.DataFrame(jsondata)
#print(datafromsite.to_string())

user = 'root'
hostip = '34.163.182.248'
passwd = 'Ciocanul12%40'
dbname = 'academy'

engine = create_engine('mysql+pymysql://root:Ciocanul12%40@34.163.182.248/academy')

"""GRAB NBA_Players from Database"""
nba_salary = pd.read_sql_query('''SELECT * FROM nba_salary''',con = engine)
nba_savings = pd.read_sql_query('''SELECT * FROM nba_savings''',con = engine)
nba_players = pd.read_sql_query('''SELECT * FROM nba_players''',con = engine)
df = nba_players

df = df.join(nba_salary['Salary'], on='index')
df = df.join(nba_savings['Savings'], on='index')
"""Push into fabian_players table at database academy"""
#df.to_sql('fabian_players', con=engine, if_exists= 'replace')


"""SUBJECT 4"""

df = df.fillna(0)

"""Exercise 4.1"""
frameone = df.groupby('team.city')['Salary'].mean().reset_index()
frameoneone = df.groupby('team.city')['index'].count().reset_index()

"""Exercise 4.2"""
frame_exercise_two = df
frame_exercise_two['full_name']= df['first_name'].astype(str) + " " + df['last_name'] #Get Full Name
frame_exercise_two = frame_exercise_two['full_name']
print(frame_exercise_two.head().to_string())

"""Exercise 4.3"""
frame_exercise_three = df[df['team.city'].str.contains("LA")]
frame_exercise_three = frame_exercise_three[['team.city','Salary']]
frame_exercise_three['full_name']=df['first_name'].astype(str) + " " + df['last_name']
frame_exercise_three = frame_exercise_three.sort_values(by='Salary', ascending=False)

print(frame_exercise_three.head().to_string())


"""
T4:
1.
city as primary id: alter table add primary key (city)
average_salary in the city: groupby(city) mean(salary)
number_of_players in the city: groupby(city) count(players)

2.
full_name of player: make dataframe with first and last name into one column
above_average_salary: query salary > mean(salary)

3.
group by city(LA) , sort by axis=1 (columns)


"""




