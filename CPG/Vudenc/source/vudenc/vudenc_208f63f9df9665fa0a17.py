def add_post(content):...
data_base = psycopg2.connect('dbname=forum')
cursor = data_base.cursor()
cursor.execute('insert into posts values (%s)', (content,))
data_base.commit()
data_base.close()
