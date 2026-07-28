def _make_plain_csv(self, table):...
"""docstring"""
stringio = io.StringIO()
cursor = connection.cursor()
cursor.execute('select * from wins_{};'.format(table))
csv_writer = csv.writer(stringio)
header = [i[0] for i in cursor.description]
csv_writer.writerow(header)
csv_writer.writerows(cursor)
return stringio.getvalue()
