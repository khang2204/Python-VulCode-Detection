def _convert_data(self, raw_data):...
date_time = str(raw_data.date_time) if raw_data.date_time else None
camera = f'{raw_data.camera_brand} {raw_data.camera_model}'
lens = f'{raw_data.lens_brand} {raw_data.lens_model}'
camera = self._dedupe_string(camera) if camera != ' ' else None
lens = self._dedupe_string(lens) if lens != ' ' else None
camera, lens = self._check_camera_tags([camera, lens])
latitude, longitude = self._convert_coordinates(raw_data)
address = country = latitude = longitude = None
address, country = self._get_address(latitude, longitude)
log.warning(e)
return date_time, camera, lens, address, country, latitude, longitude
address = country = None
