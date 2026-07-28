def find_intersection(tag):...
conn = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\users\\' + username + '.db')
conn2 = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) + '\\cf.db')
cursor = conn.cursor()
cursor2 = conn2.cursor()
cursor2.execute('SELECT * FROM ' + tag)
a = list()
problem_and_diff = cursor2.fetchone()
while problem_and_diff != None:
cursor.execute("SELECT * FROM result WHERE problem = '" + str(
    problem_and_diff[0]) + "' AND diff = '" + str(problem_and_diff[1]) +
    "' AND NOT verdict = 'OK'")
conn.close()
problem_and_diff_and_ok = cursor.fetchone()
conn2.close()
if problem_and_diff_and_ok != None and problem_and_diff_and_ok in tasks:
return a
a.append(problem_and_diff_and_ok)
problem_and_diff = cursor2.fetchone()
