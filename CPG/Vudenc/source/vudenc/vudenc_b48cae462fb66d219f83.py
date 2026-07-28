def drop():...
co = connect()
cu = co.cursor()
cu.execute('DROP TABLE IF EXISTS players CASCADE;')
cu.execute('DROP TABLE IF EXISTS matches CASCADE;')
co.commit()
cu.close()
co.close()
return 0
