def generate_bno(self):...
query = 'SELECT MAX(bno) FROM bookings'
self.cursor.execute(query)
max_bno = self.cursor.fetchone()
return int(max_bno[0]) + 1
