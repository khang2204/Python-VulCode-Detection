@Throttle(MIN_TIME_BETWEEN_UPDATES)...
"""docstring"""
import pyatmo
self.station_data = pyatmo.WeatherStationData(self.auth)
if self.station is not None:
self.data = self.station_data.lastData(station=self.station, exclude=3600)
self.data = self.station_data.lastData(exclude=3600)
