def _convert_coordinates(self, raw_data):...
"""docstring"""
latitude = self._get_dd_coordinate(raw_data.raw_latitude, raw_data.
    latitude_reference)
log.error(e)
return latitude, longitude
longitude = self._get_dd_coordinate(raw_data.raw_longitude, raw_data.
    longitude_reference)
log.error('Cannot read coordinates of this photo.')
raw_coordinates = f"""Latitude reference: {raw_data.latitude_reference}
Raw latitude: {raw_data.raw_latitude}.
Longitude reference: {raw_data.longitude_reference} Raw longitude: {raw_data.raw_longitude}.
"""
log.info(raw_coordinates)
