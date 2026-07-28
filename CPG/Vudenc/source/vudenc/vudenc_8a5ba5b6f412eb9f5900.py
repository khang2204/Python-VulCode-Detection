def check_heroku_db():...
if 'DATABASE_URL' in os.environ and os.environ['DATABASE_URL']:
urllib.parse.uses_netloc.append('postgres')
conn = psycopg2.connect(database='expenses')
url = urllib.parse.urlparse(os.environ['DATABASE_URL'])
return conn
conn = psycopg2.connect(database=url.path[1:], user=url.username, password=
    url.password, host=url.hostname, port=url.port)
return conn
