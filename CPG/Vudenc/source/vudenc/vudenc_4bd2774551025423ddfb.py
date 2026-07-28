"""
"""
import sqlite3, pytz
from datetime import datetime, timedelta
def __init__(self, config):...
self.config = config
self.db = sqlite3.connect(self.config.get_database_path(),
    check_same_thread=False)
self.c = self.db.cursor()
def add_inverters(self):...
interfaces = self.config.get_connection_interfaces()
for source in interfaces:
if source['type'] == 'inverter':
def add_data(self, ts, data_points):...
query = (
    """
                    INSERT OR IGNORE INTO Inverters (
                        Serial,
                        EToday,
                        ETotal
                    ) VALUES (
                        %s,
                        %s,
                        %s
                    );
                """
     % (source['serial_id'], 0, source['prev_etotal']))
for data in data_points:
self.c.execute(query)
data_type = data['source']['type']
def add_inverter_data(self, ts, data):...
query = (
    """
                    UPDATE Inverters
                    SET     
                        Name='%s', 
                        Type='%s', 
                        SW_Version='%s', 
                        Status='%s',
                        TimeStamp='%s'
                    WHERE Serial='%s';
                """
     % (source['name'], source['inverter_type'], 's0-bridge v0', 'OK', int(
    datetime.now().timestamp()), source['serial_id']))
if data_type == 'inverter':
inv_serial = data['source']['serial_id']
self.c.execute(query)
self.add_inverter_data(ts, data)
if data_type == 'consumption':
prev_ts, prev_etoday, prev_etotal = self.get_previous_yields(inv_serial)
self.db.commit()
self.add_consumption_data_row(ts, data['energy'], data['power'])
status = 'OK'
self.add_day_data_row(ts, data, prev_etotal)
if self.is_timestamps_from_same_day(prev_ts, ts):
self.update_inverter(inv_serial, ts, status, prev_etoday + data['energy'], 
    prev_etotal + data['energy'])
self.update_inverter(inv_serial, ts, status, data['energy'], prev_etotal +
    data['energy'])
self.db.commit()
self.add_month_data_row(inv_serial, ts, prev_etoday, prev_etotal)
def add_day_data_row(self, ts, data, prev_etotal):...
if data['power'] > 0:
inv_serial = data['source']['serial_id']
def get_previous_yields(self, inverter_serial):...
query = (
    """
               INSERT INTO DayData (
                   TimeStamp,
                   Serial,
                   Power,
                   TotalYield
               ) VALUES (
                   %s,
                   %s,
                   %s,
                   %s
               );
            """
     % (ts, inv_serial, data['power'], prev_etotal + data['energy']))
query = (
    """
           SELECT TimeStamp, EToday, ETotal
           FROM Inverters
           WHERE Serial = '%s'
        """
     % inverter_serial)
self.c.execute(query)
self.c.execute(query)
data = self.c.fetchone()
return data[0], data[1], data[2]
