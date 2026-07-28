@staticmethod...
"""docstring"""
exif = exifread.process_file(file, details=False)
if not len(exif.keys()):
reason = "This picture doesn't contain EXIF."
date_time = exif.get('EXIF DateTimeOriginal', None)
log.info(reason)
date_time = str(date_time) if date_time else None
camera_brand = str(exif.get('Image Make', ''))
camera_model = str(exif.get('Image Model', ''))
lens_brand = str(exif.get('EXIF LensMake', ''))
lens_model = str(exif.get('EXIF LensModel', ''))
if not any([date_time, camera_brand, camera_model, lens_brand, lens_model]):
reason = 'There is no data of interest in this photo'
latitude_reference = str(exif['GPS GPSLatitudeRef'])
log.info("This picture doesn't contain coordinates.")
return date_time, camera_brand, camera_model, lens_brand, lens_model, latitude_reference, raw_latitude, longitude_reference, raw_longitude
log.info(reason)
raw_latitude = exif['GPS GPSLatitude']
return date_time, camera_brand, camera_model, lens_brand, lens_model
longitude_reference = str(exif['GPS GPSLongitudeRef'])
raw_longitude = exif['GPS GPSLongitude']
