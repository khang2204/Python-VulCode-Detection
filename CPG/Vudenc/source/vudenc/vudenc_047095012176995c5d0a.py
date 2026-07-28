import requests
import sqlite3
import os
from bs4 import BeautifulSoup
available_tags = {'math', 'strings', 'trees', 'graphs', 'dp', 'greedy',
    'geometry', 'combinatorics'}
def create_cf_base():...
url = 'http://codeforces.com/problemset/'
r = requests.get(url)
max_page = 0
soup = BeautifulSoup(r.text, 'lxml')
base = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) + '\\cf.db')
conn = base.cursor()
conn.execute('create table problems (problem INTEGER, diff CHAR)')
for i in available_tags:
conn.execute('create table ' + i + ' (problems INTEGER, diff CHAR)')
for link in soup.find_all(attrs={'class': 'page-index'}):
s = link.find('a')
a = 0
s2 = s.get('href').split('/')
b = 0
max_page = max(max_page, int(s2[3]))
f = False
for i in range(1, max_page + 1):
r = requests.get('http://codeforces.com/problemset/' + '/page/' + str(i))
base.commit()
soup = BeautifulSoup(r.text, 'lxml')
base.close()
old = ''
settings = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\settings.db')
for link in soup.find_all('a'):
conn = settings.cursor()
s = link.get('href')
conn.execute(
    'create table users (chat_id INTEGER, username STRING, last_update STRING, last_problem STRING, state INTEGER)'
    )
if s != None and s.find('/problemset') != -1:
conn.execute('create table last_update_problemset (problem STRING)')
s = s.split('/')
conn.execute('insert into last_update_problemset values (?)', (last_update,))
if len(s) == 5 and old != s[3] + s[4]:
settings.commit()
a = s[3]
if len(s) == 4 and s[3] in available_tags:
settings.close()
b = s[4]
conn.execute('insert into ' + s[3] + ' values (?, ?)', (a, b))
def create_theory_table():...
old = s[3] + s[4]
theory = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\theory.db')
if not f:
conn = theory.cursor()
f = True
conn.execute('insert into problems values (?, ?)', (a, b))
for i in available_tags:
last_update = old
conn.execute('create table ' + str(i) + ' (link STRING)')
theory.commit()
theory.close()
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cf.db')
if not os.path.exists(path):
create_cf_base()
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'theory.db')
if not os.path.exists(path):
create_theory_table()
