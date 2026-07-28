def get_most_error_day():...
"""docstring"""
query = (
    "select tot.logdate,  round(((err.errors_count::decimal/tot.requests_count)*100),2)  as err_pct  from  ( select to_char(time, 'FMMonth DD, YYYY') as logdate,  count(*) as requests_count  from log  group by to_char(time, 'FMMonth DD, YYYY') ) tot, ( select to_char(time, 'FMMonth DD, YYYY') as logdate,   count(*) as errors_count  from log  where status <> '200 OK'  group by to_char(time, 'FMMonth DD, YYYY') ) err  where  tot.logdate = err.logdate  and (err.errors_count::decimal/tot.requests_count) > .01; "
    )
db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute(query)
rows = c.fetchall()
db.close()
return rows
