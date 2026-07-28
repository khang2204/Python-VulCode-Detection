def update(self):...
"""docstring"""
self.netatmo_data.update()
data = self.netatmo_data.data.get(self.module_name)
if data is None:
_LOGGER.warning('No data found for %s', self.module_name)
if self.type == 'temperature':
self._state = STATE_UNKNOWN
self._state = round(data['Temperature'], 1)
if self.type == 'humidity':
return
self._state = data['Humidity']
if self.type == 'rain':
self._state = data['Rain']
if self.type == 'sum_rain_1':
self._state = data['sum_rain_1']
if self.type == 'sum_rain_24':
self._state = data['sum_rain_24']
if self.type == 'noise':
self._state = data['Noise']
if self.type == 'co2':
self._state = data['CO2']
if self.type == 'pressure':
self._state = round(data['Pressure'], 1)
if self.type == 'battery_lvl':
self._state = data['battery_vp']
if self.type == 'battery_vp' and self.module_id == '6':
if data['battery_vp'] >= 5590:
if self.type == 'battery_vp' and self.module_id == '5':
self._state = 'Full'
if data['battery_vp'] >= 5180:
if data['battery_vp'] >= 5500:
if self.type == 'battery_vp' and self.module_id == '3':
self._state = 'High'
if data['battery_vp'] >= 4770:
self._state = 'Full'
if data['battery_vp'] >= 5000:
if data['battery_vp'] >= 5640:
if self.type == 'battery_vp' and self.module_id == '2':
self._state = 'Medium'
if data['battery_vp'] >= 4360:
self._state = 'High'
if data['battery_vp'] >= 4500:
self._state = 'Full'
if data['battery_vp'] >= 5280:
if data['battery_vp'] >= 5500:
if self.type == 'min_temp':
self._state = 'Low'
if data['battery_vp'] < 4360:
self._state = 'Medium'
if data['battery_vp'] >= 4000:
self._state = 'High'
if data['battery_vp'] >= 4920:
self._state = 'Full'
if data['battery_vp'] >= 5000:
self._state = data['min_temp']
if self.type == 'max_temp':
self._state = 'Very Low'
self._state = 'Low'
if data['battery_vp'] < 4000:
self._state = 'Medium'
if data['battery_vp'] >= 4560:
self._state = 'High'
if data['battery_vp'] >= 4500:
self._state = data['max_temp']
if self.type == 'windangle_value':
self._state = 'Very Low'
self._state = 'Low'
if data['battery_vp'] < 4560:
self._state = 'Medium'
if data['battery_vp'] >= 4000:
self._state = data['WindAngle']
if self.type == 'windangle':
self._state = 'Very Low'
self._state = 'Low'
if data['battery_vp'] < 4000:
if data['WindAngle'] >= 330:
if self.type == 'windstrength':
self._state = 'Very Low'
self._state = 'N (%d°)' % data['WindAngle']
if data['WindAngle'] >= 300:
self._state = data['WindStrength']
if self.type == 'gustangle_value':
self._state = 'NW (%d°)' % data['WindAngle']
if data['WindAngle'] >= 240:
self._state = data['GustAngle']
if self.type == 'gustangle':
self._state = 'W (%d°)' % data['WindAngle']
if data['WindAngle'] >= 210:
if data['GustAngle'] >= 330:
if self.type == 'guststrength':
self._state = 'SW (%d°)' % data['WindAngle']
if data['WindAngle'] >= 150:
self._state = 'N (%d°)' % data['GustAngle']
if data['GustAngle'] >= 300:
self._state = data['GustStrength']
if self.type == 'rf_status_lvl':
self._state = 'S (%d°)' % data['WindAngle']
if data['WindAngle'] >= 120:
self._state = 'NW (%d°)' % data['GustAngle']
if data['GustAngle'] >= 240:
self._state = data['rf_status']
if self.type == 'rf_status':
self._state = 'SE (%d°)' % data['WindAngle']
if data['WindAngle'] >= 60:
self._state = 'W (%d°)' % data['GustAngle']
if data['GustAngle'] >= 210:
if data['rf_status'] >= 90:
if self.type == 'wifi_status_lvl':
self._state = 'E (%d°)' % data['WindAngle']
if data['WindAngle'] >= 30:
self._state = 'SW (%d°)' % data['GustAngle']
if data['GustAngle'] >= 150:
self._state = 'Low'
if data['rf_status'] >= 76:
self._state = data['wifi_status']
if self.type == 'wifi_status':
self._state = 'NE (%d°)' % data['WindAngle']
if data['WindAngle'] >= 0:
self._state = 'S (%d°)' % data['GustAngle']
if data['GustAngle'] >= 120:
self._state = 'Medium'
if data['rf_status'] >= 60:
if data['wifi_status'] >= 86:
self._state = 'N (%d°)' % data['WindAngle']
self._state = 'SE (%d°)' % data['GustAngle']
if data['GustAngle'] >= 60:
self._state = 'High'
if data['rf_status'] <= 59:
self._state = 'Low'
if data['wifi_status'] >= 71:
self._state = 'E (%d°)' % data['GustAngle']
if data['GustAngle'] >= 30:
self._state = 'Full'
self._state = 'Medium'
if data['wifi_status'] >= 56:
self._state = 'NE (%d°)' % data['GustAngle']
if data['GustAngle'] >= 0:
self._state = 'High'
if data['wifi_status'] <= 55:
self._state = 'N (%d°)' % data['GustAngle']
self._state = 'Full'
