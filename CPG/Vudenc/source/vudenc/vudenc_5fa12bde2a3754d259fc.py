"""
"""
import pytz
import sqlite3
from datetime import datetime, timedelta
def __init__(self, config):...
self.config = config
self.co2_mult = self.config.get_co2_avoidance_factor()
self.db = sqlite3.connect(self.config.get_database_path(),
    check_same_thread=False)
self.c = self.db.cursor()
self.local_timezone = self.get_local_timezone()
def get(self, date):...
data = dict()
data['today'] = self.get_today()
data['requested'] = self.get_requested(date)
return data
