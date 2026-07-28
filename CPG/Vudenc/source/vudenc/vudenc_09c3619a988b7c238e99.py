def add_inverter_data(self, ts, data):...
inv_serial = data['source']['serial_id']
prev_ts, prev_etoday, prev_etotal = self.get_previous_yields(inv_serial)
status = 'OK'
self.add_day_data_row(ts, data, prev_etotal)
if self.is_timestamps_from_same_day(prev_ts, ts):
self.update_inverter(inv_serial, ts, status, prev_etoday + data['energy'], 
    prev_etotal + data['energy'])
self.update_inverter(inv_serial, ts, status, data['energy'], prev_etotal +
    data['energy'])
self.db.commit()
self.add_month_data_row(inv_serial, ts, prev_etoday, prev_etotal)
