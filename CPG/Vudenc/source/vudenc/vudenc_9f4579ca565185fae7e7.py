def init_user(username, chat_id):...
conn = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\users\\' + username + '.db')
conn2 = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) + '\\cf.db')
cursor = conn.cursor()
cursor2 = conn2.cursor()
cursor.execute(
    'CREATE TABLE result (problem INTEGER, diff STRING, verdict STRING)')
cursor2.execute('SELECT * FROM problems')
x = cursor2.fetchone()
while x != None:
cursor.execute('insert into result values (?, ?, ? )', (x[0], x[1], 'NULL'))
url = 'http://codeforces.com/submissions/' + username
x = cursor2.fetchone()
r = requests.get(url)
max_page = 1
soup = BeautifulSoup(r.text, 'lxml')
for link in soup.find_all(attrs={'class': 'page-index'}):
s = link.find('a')
old = ''
s2 = s.get('href').split('/')
r = requests.get('http://codeforces.com/submissions/' + username + '/page/0')
max_page = max(max_page, int(s2[4]))
soup = BeautifulSoup(r.text, 'lxml')
last_try = soup.find(attrs={'class': 'status-small'})
if not last_try == None:
last_try = str(last_try).split()
for i in range(1, max_page + 1):
last_try = str(last_try[2]) + str(last_try[3])
r = requests.get('http://codeforces.com/submissions/' + username + '/page/' +
    str(i))
conn.commit()
soup = BeautifulSoup(r.text, 'lxml')
conn.close()
count = 0
conn2.close()
ver = soup.find_all(attrs={'class': 'submissionVerdictWrapper'})
settings = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\settings.db')
for link in soup.find_all('a'):
conn = settings.cursor()
s = link.get('href')
conn.execute('select * from last_update_problemset')
if s != None and s.find('/problemset') != -1:
last_problem = conn.fetchone()
s = s.split('/')
conn.execute("select * from users where chat_id = '" + str(chat_id) + "'")
if len(s) == 5:
x = conn.fetchone()
s2 = str(ver[count]).split()
if x == None:
s2 = s2[5].split('"')
conn.execute('insert into users values (?, ?, ?, ?, ?)', (chat_id, username,
    str(last_try), str(last_problem[0]), 1))
conn.execute("update users set username = '" + str(username) +
    "' where chat_id = '" + str(chat_id) + "'")
count += 1
settings.commit()
conn.execute("update users set last_update = '" + str(last_try) +
    "' where chat_id = '" + str(chat_id) + "'")
cursor.execute("select * from result where problem = '" + s[3] +
    "'and diff = '" + s[4] + "'")
settings.close()
conn.execute("update users set last_problem = '" + str(last_problem[0]) +
    "' where chat_id = '" + str(chat_id) + "'")
x = cursor.fetchone()
conn.execute("update users set state = '" + str(1) + "' where chat_id = '" +
    str(chat_id) + "'")
if s2[1] == 'OK' and x != None:
cursor.execute("update result set verdict = '" + s2[1] +
    "' where problem = '" + s[3] + "' and diff = '" + s[4] + "'")
if x != None and x[2] != 'OK':
cursor.execute("update result set verdict = '" + s2[1] +
    "' where problem = '" + s[3] + "' and diff = '" + s[4] + "'")
