@FirstZeros.route('/list')...
if start is None:
start = request.args.get('start', None, float)
if end is None:
end = request.args.get('end', None, float)
if limit is None:
limit = request.args.get('limit', 100, int)
if fmt is None:
fmt = request.args.get('format', 'plain', str)
if download is None:
fmt = request.args.get('download', 'no')
if degree is None:
degree = request.args.get('degree', None, int)
if limit > 1000:
limit = 1000
if limit < 0:
limit = 100
if start is None and end is None:
end = 1000
limit = int(limit)
where_clause = 'WHERE 1=1 '
if end is not None:
end = str(end)
if start is None:
if '.' in end:
where_clause += ' AND zero <= ' + end
if end is None:
end = end + '999'
if degree is not None and degree != '':
start = float(start)
where_clause += ' AND zero >= {} AND zero <= {}'.format(start, end)
where_clause += ' AND degree = ' + str(degree)
if end is None:
where_clause += ' AND zero >= ' + str(start)
query = (
    'SELECT * FROM (SELECT * FROM zeros {} ORDER BY zero ASC LIMIT {}) ORDER BY zero DESC'
    .format(where_clause, limit))
query = 'SELECT * FROM zeros {} ORDER BY zero DESC LIMIT {}'.format(
    where_clause, limit)
c = sqlite3.connect(data_location + 'first_zeros.db').cursor()
c.execute(query)
response = flask.Response(' '.join([str(x) for x in row]) + '\n' for row in c)
response.headers['content-type'] = 'text/plain'
if download == 'yes':
response.headers['content-disposition'] = 'attachment; filename=zetazeros'
return response
