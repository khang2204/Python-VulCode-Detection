"""
desc: application for end users to access retail data
"""
import queries
import configparser
import customer_commands
import help_functions
def init():...
config = configparser.ConfigParser()
config.read('config.ini')
return queries.Query(host=config['database']['host'], dbname=config[
    'database']['dbname'], user=config['database']['user'], password=config
    ['database']['pass'])
