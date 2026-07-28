def init():...
config = configparser.ConfigParser()
config.read('config.ini')
return queries.Query(host=config['database']['host'], dbname=config[
    'database']['dbname'], user=config['database']['user'], password=config
    ['database']['pass'])
