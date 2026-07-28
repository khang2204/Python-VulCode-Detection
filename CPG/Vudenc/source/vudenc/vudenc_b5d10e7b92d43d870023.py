def create_text_stats(username):...
verdict = {'COMPILATION_ERROR': 0, 'OK': 0, 'TIME_LIMIT_EXCEEDED': 0,
    'WRONG_ANSWER': 0, 'RUNTIME_ERROR': 0, 'MEMORY_LIMIT_EXCEEDED': 0}
colors = ['red', 'green', 'tan', 'blue', 'purple', 'orange']
conn = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\users\\' + username + '.db')
conn2 = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) + '\\cf.db')
cursor = conn.cursor()
cursor2 = conn2.cursor()
count = 0
a = list()
b = list()
for i in available_tags:
cursor2.execute('SELECT * FROM ' + str(i))
for i in verdict.keys():
x = cursor2.fetchone()
a.append(i)
fig1, ax1 = plt.subplots()
while x != None:
b.append(verdict[i])
ax1.pie(b, labels=b, colors=colors, shadow=True, startangle=90)
cursor.execute("SELECT * FROM result WHERE problem = '" + str(x[0]) +
    "' AND diff = '" + str(x[1]) + "'")
ax1.axis('equal')
y = cursor.fetchone()
ax1.legend(a)
if y != None:
ax1.set_title('How many different verdict in last status of problem you have: '
    )
for j in verdict.keys():
x = cursor2.fetchone()
path = os.path.join(os.path.abspath(os.path.dirname(__file__)) +
    '\\users\\', username + '.png')
if y[2] == j:
if os.path.exists(path):
verdict[j] += 1
os.remove(path)
plt.savefig(os.path.abspath(os.path.dirname(__file__)) + '\\users\\' +
    username + '.png')
count += 1
conn.close()
conn2.close()
plt.close()
s = username + ' has at least one submissions in ' + str(count) + ' problems'
return s
