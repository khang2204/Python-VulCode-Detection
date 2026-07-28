import psycopg2
import consts
from metrics.Network.partition import partition_bots, partition_groups
from sentiment_analysis import sentiment_compound_score
connection = psycopg2.connect(**consts.db_creds)
def get_edges(users):...
user_dict = {}
for i in users:
user_dict[i] = 1
cursor = connection.cursor()
drop_old = 'DELETE FROM temp'
connection.commit()
cursor.execute(drop_old)
insert = """INSERT INTO temp (usr)
                 VALUES (%s);"""
for user in user_dict:
cursor.execute(insert, [user])
connection.commit()
select = """ SELECT influences.usr, influences.other_usr
                 FROM influences
                 INNER JOIN temp as t1
                 ON t1.usr = influences.usr AND influences.usr != influences.other_usr
                 INNER JOIN temp as t2
                 ON t2.usr = influences.other_usr"""
cursor.execute(select)
edges = []
fetched = [None]
while len(fetched) > 0:
fetched = cursor.fetchall()
cursor.execute(drop_old)
edges.extend(fetched)
connection.commit()
return edges
