def get_error_days(cur, error_percent):...
"""docstring"""
query = (
    """SELECT to_char(log_errors.date, 'Mon DD YYYY'),
            round((log_errors.errors * 100
            / log_requests.total::numeric), 2) as percent
            FROM log_errors, log_requests
            WHERE log_errors.date = log_requests.date AND
            log_errors.errors * 100
            / log_requests.total::numeric > {}
            ORDER BY log_errors.date"""
    .format(error_percent))
rows = get_data(cur, query)
if rows is not None:
file = open('error_report.txt', 'w')
return False
for row in rows:
file.write('{} - {}% errors \n'.format(row[0], row[1]))
file.close()
return True
