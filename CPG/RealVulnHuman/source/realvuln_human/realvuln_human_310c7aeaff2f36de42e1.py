import json
import base64

import geoip2.database

from cryptography.fernet import Fernet


key = 'JHtM1wEt1I1J9N_Evjwqr3yYauXIqSxYzFnRhcf0ZG0='
fernet = Fernet(key)
ttl = 7200 # seconds
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')


def getcountry(request):

    country = 'XX' # For local connections

    try:
