def add_data(self, ts, data_points):...
for data in data_points:
data_type = data['source']['type']
if data_type == 'inverter':
self.add_inverter_data(ts, data)
if data_type == 'consumption':
self.add_consumption_data_row(ts, data['energy'], data['power'])
