def create_stats_picture(username):...
conn = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\users\\' + username + '.db')
conn2 = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) + '\\cf.db')
cursor = conn.cursor()
cursor2 = conn2.cursor()
a = list()
b = list()
leg = list()
sum = 0
for i in available_tags:
cursor2.execute('SELECT * FROM ' + str(i))
conn.close()
x = cursor2.fetchone()
conn2.close()
count = 0
if sum == 0:
while x != None:
return True
for i in range(len(a)):
cursor.execute("SELECT * FROM result WHERE problem = '" + str(x[0]) +
    "' AND diff = '" + str(x[1]) + "' AND verdict = 'OK'")
a.append(Pair(count, i))
if a[i].first / sum != 0:
fig1, ax1 = plt.subplots()
y = cursor.fetchone()
sum += count
b.append(a[i].first / sum)
ax1.pie(b, autopct='%1.1f%%', shadow=True, startangle=90)
if y != None:
leg.append(a[i].second)
ax1.axis('equal')
count += 1
x = cursor2.fetchone()
ax1.legend(leg)
path = os.path.join(os.path.abspath(os.path.dirname(__file__)) +
    '\\users\\', username + '.png')
if os.path.exists(path):
os.remove(path)
plt.savefig(os.path.abspath(os.path.dirname(__file__)) + '\\users\\' +
    username + '.png')
plt.close()
return False
