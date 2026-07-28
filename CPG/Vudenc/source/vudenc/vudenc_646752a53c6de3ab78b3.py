def get_inverters(self):...
query = """
            SELECT Serial, Name, Type, TimeStamp, EToday, ETotal, Status, OperatingTime
            FROM Inverters;
            """
invs = []
renamings = self.config.get_renamings()
for row in self.c.execute(query):
serial = str(row[0])
return invs
name = row[1]
if serial in renamings.keys():
name = renamings[serial]
invs.append({'serial': serial, 'name': name, 'type': row[2], 'ts': row[3],
    'etoday': row[4], 'etotal': row[5], 'status': row[6]})
