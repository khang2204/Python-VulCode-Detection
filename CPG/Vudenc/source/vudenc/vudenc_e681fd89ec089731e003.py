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
if module_name not in data.get_module_names():
for variable in data.station_data.monitoredConditions(module_name):
_LOGGER.error('Module name: "%s" not found', module_name)
for variable in monitored_conditions:
if variable in SENSOR_TYPES.keys():
dev.append(NetAtmoSensor(data, module_name, variable))
dev.append(NetAtmoSensor(data, module_name, variable))
_LOGGER.warning('Ignoring unknown var %s for mod %s', variable, module_name)
