"""
Support for the NetAtmo Weather Service.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/sensor.netatmo/
"""
import logging
from datetime import timedelta
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import TEMP_CELSIUS, DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_TEMPERATURE, STATE_UNKNOWN
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
import homeassistant.helpers.config_validation as cv
_LOGGER = logging.getLogger(__name__)
CONF_MODULES = 'modules'
CONF_STATION = 'station'
DEPENDENCIES = ['netatmo']
MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=600)
SENSOR_TYPES = {'temperature': ['Temperature', TEMP_CELSIUS, None,
    DEVICE_CLASS_TEMPERATURE], 'co2': ['CO2', 'ppm', 'mdi:cloud', None],
    'pressure': ['Pressure', 'mbar', 'mdi:gauge', None], 'noise': ['Noise',
    'dB', 'mdi:volume-high', None], 'humidity': ['Humidity', '%', None,
    DEVICE_CLASS_HUMIDITY], 'rain': ['Rain', 'mm', 'mdi:weather-rainy',
    None], 'sum_rain_1': ['sum_rain_1', 'mm', 'mdi:weather-rainy', None],
    'sum_rain_24': ['sum_rain_24', 'mm', 'mdi:weather-rainy', None],
    'battery_vp': ['Battery', '', 'mdi:battery', None], 'battery_lvl': [
    'Battery_lvl', '', 'mdi:battery', None], 'min_temp': ['Min Temp.',
    TEMP_CELSIUS, 'mdi:thermometer', None], 'max_temp': ['Max Temp.',
    TEMP_CELSIUS, 'mdi:thermometer', None], 'windangle': ['Angle', '',
    'mdi:compass', None], 'windangle_value': ['Angle Value', 'º',
    'mdi:compass', None], 'windstrength': ['Strength', 'km/h',
    'mdi:weather-windy', None], 'gustangle': ['Gust Angle', '',
    'mdi:compass', None], 'gustangle_value': ['Gust Angle Value', 'º',
    'mdi:compass', None], 'guststrength': ['Gust Strength', 'km/h',
    'mdi:weather-windy', None], 'rf_status': ['Radio', '', 'mdi:signal',
    None], 'rf_status_lvl': ['Radio_lvl', '', 'mdi:signal', None],
    'wifi_status': ['Wifi', '', 'mdi:wifi', None], 'wifi_status_lvl': [
    'Wifi_lvl', 'dBm', 'mdi:wifi', None]}
MODULE_SCHEMA = vol.Schema({vol.Required(cv.string): vol.All(cv.ensure_list,
    [vol.In(SENSOR_TYPES)])})
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({vol.Optional(CONF_STATION): cv.
    string, vol.Optional(CONF_MODULES): MODULE_SCHEMA})
def setup_platform(hass, config, add_devices, discovery_info=None):...
"""docstring"""
netatmo = hass.components.netatmo
data = NetAtmoData(netatmo.NETATMO_AUTH, config.get(CONF_STATION, None))
dev = []
import pyatmo
if CONF_MODULES in config:
return None
add_devices(dev, True)
for module_name, monitored_conditions in config[CONF_MODULES].items():
for module_name in data.get_module_names():
"""Implementation of a Netatmo sensor."""
if module_name not in data.get_module_names():
for variable in data.station_data.monitoredConditions(module_name):
def __init__(self, netatmo_data, module_name, sensor_type):...
_LOGGER.error('Module name: "%s" not found', module_name)
for variable in monitored_conditions:
if variable in SENSOR_TYPES.keys():
"""docstring"""
dev.append(NetAtmoSensor(data, module_name, variable))
dev.append(NetAtmoSensor(data, module_name, variable))
_LOGGER.warning('Ignoring unknown var %s for mod %s', variable, module_name)
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
@property...
"""docstring"""
return self._name
