def get_report(self, reportID):...
query = 'SELECT * FROM report WHERE Report_ID = ' + reportID
self.cursor.execute(query)
self.connection.commit()
fetch = self.cursor.fetchone()
report = ' '.join(map(str, fetch))
return report
