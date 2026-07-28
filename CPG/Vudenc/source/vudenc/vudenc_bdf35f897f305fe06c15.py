from dataclasses import dataclass
from typing import Dict
import exifread
from exifread.classes import IfdTag
from geopy.geocoders import Nominatim
from photogpsbot import bot, log, db, User
"""
    Coordinates have invalid format
    """
"""
    There is no location info
    """
"""
    Means that there is no EXIF within the photo at all

    """
"""
    Means that there is actually no any data of our interest within the picture

    """
"""
    A class to store info about a photo from user.
    """
user: User
date_time: str = None
camera: str = None
lens: str = None
address: str = None
country: Dict[str, str] = None
latitude: float = None
longitude: float = None
"""
    Raw data from photo that is still have to be converted in order to be used.
    """
user: User
date_time: str = None
camera_brand: str = None
camera_model: str = None
lens_brand: str = None
lens_model: str = None
latitude_reference: str = None
raw_latitude: IfdTag = None
longitude_reference: str = None
raw_longitude: IfdTag = None
def __init__(self, user, file):...
self.user = user
self.file = file
self.raw_data = None
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
@staticmethod...
"""docstring"""
deduped_string = ''
for x in string.split(' '):
if x not in deduped_string:
return deduped_string.rstrip()
deduped_string += x + ' '
