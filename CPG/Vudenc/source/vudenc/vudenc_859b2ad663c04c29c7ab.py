def create_theory_table():...
theory = sqlite3.connect(os.path.abspath(os.path.dirname(__file__)) +
    '\\theory.db')
conn = theory.cursor()
for i in available_tags:
conn.execute('create table ' + str(i) + ' (link STRING)')
theory.commit()
theory.close()
