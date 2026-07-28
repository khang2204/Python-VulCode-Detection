def get_requested(self, date):...
data = dict()
data['date'] = date
data['all'] = dict()
data['all']['day'] = self.get_requested_day(date)
data['all']['month'] = self.get_requested_month(date)
data['inverters'] = dict()
inverters = self.get_inverters()
for inv in inverters:
data['inverters'][inv['serial']] = {'day': [], 'month': []}
return data
data['inverters'][inv['serial']]['day'] = self.get_requested_day_for_inverter(
    inv['serial'], date)
data['inverters'][inv['serial']]['month'
    ] = self.get_requested_month_for_inverter(inv['serial'], date)
