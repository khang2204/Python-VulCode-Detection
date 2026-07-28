def truncate(table):...
co = connect()
cu = co.cursor()
cu.execute('TRUNCATE ' + table + ';')
co.commit()
cu.close()
co.close()
