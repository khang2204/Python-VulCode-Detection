from gfui.backends.default import Backend
import mysql.connector
from gfui.chartgraph import Graph, Table
import re
import ipaddress
import os
def __init__(self, OPTIONS):...
super().__init__()
self.required_opts = ['SQL_SERVER', 'SQL_USERNAME', 'SQL_DB']
self.parse_options(OPTIONS)
self.columns = {}
pw = os.environ.get('SQL_PASSWORD')
if not pw:
pw = self.OPTIONS['SQL_PASSWORD']
self.db = mysql.connector.connect(host=self.OPTIONS['SQL_SERVER'], user=
    self.OPTIONS['SQL_USERNAME'], passwd=pw)
self.schema = Schema()
self.filters = []
def get_columns(self):...
return self.schema.get_columns()
