def get_today(self):...
data = dict()
total_day = 0
total = 0
co2 = 0
data['inverters'] = dict()
inverters = self.get_inverters()
for inv in inverters:
inv_co2 = 0
data['dayTotal'] = total_day
if inv['etotal'] is not None:
data['total'] = total
inv_co2 = round(inv['etotal'] / 1000 * self.co2_mult)
data['inverters'][inv['serial']] = {'serial': inv['serial'], 'name': inv[
    'name'], 'lastUpdated': inv['ts'], 'dayTotal': inv['etoday'], 'total':
    inv['etotal'], 'status': inv['status'], 'co2': inv_co2}
data['co2'] = co2
if inv['etoday'] is not None:
return data
total_day += inv['etoday']
if inv['etotal'] is not None:
total += inv['etotal']
co2 += inv_co2
