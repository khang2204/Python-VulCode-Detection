def get_theory_from_tag(tag):...
if not tag in available_tags:
return 'Incorrect tag.'
base = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\theory.db')
conn = base.cursor()
conn.execute('select * from ' + tag)
x = conn.fetchone()
s = ''
while x != None:
s += str(x[0]) + '\n'
base.close()
x = conn.fetchone()
return s
