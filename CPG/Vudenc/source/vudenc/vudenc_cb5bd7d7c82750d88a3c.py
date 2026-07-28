@staticmethod...
"""docstring"""
address = {}
country = {}
coordinates = f'{latitude}, {longitude}'
log.debug('Getting address from coordinates %s...', coordinates)
geolocator = Nominatim()
location = geolocator.reverse(coordinates, language='en')
log.error('Getting address has failed!')
address['en-US'] = location.address
log.error(e)
country['en-US'] = location.raw['address']['country']
location2 = geolocator.reverse(coordinates, language='ru')
address['ru-RU'] = location2.address
country['ru-RU'] = location2.raw['address']['country']
return address, country
