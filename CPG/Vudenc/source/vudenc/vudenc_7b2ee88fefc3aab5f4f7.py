def __init__(self, netatmo_data, module_name, sensor_type):...
"""docstring"""
self._name = 'Netatmo {} {}'.format(module_name, SENSOR_TYPES[sensor_type][0])
self.netatmo_data = netatmo_data
self.module_name = module_name
self.type = sensor_type
self._state = None
self._device_class = SENSOR_TYPES[self.type][3]
self._icon = SENSOR_TYPES[self.type][2]
self._unit_of_measurement = SENSOR_TYPES[self.type][1]
module_id = self.netatmo_data.station_data.moduleByName(module=module_name)[
    '_id']
self.module_id = module_id[1]
