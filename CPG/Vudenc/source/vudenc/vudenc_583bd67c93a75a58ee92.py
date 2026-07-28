def get_image_info(self):...
"""docstring"""
raw_data = RawImageData(self.user, *self._get_raw_data(self.file))
image_data = ImageData(self.user, *self._convert_data(raw_data))
return image_data
