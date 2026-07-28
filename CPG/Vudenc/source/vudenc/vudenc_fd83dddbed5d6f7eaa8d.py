import urllib, re, html
from settings import MAX_BASENAME_LENGTH, ITEMS_PER_PAGE, PASSWORD_KEY, SECRET_KEY, BASE_URL, BASE_URL_ROOT
from core.libs.bottle import redirect, response
import hashlib, base64
from core.libs.bottle import _stderr
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def default(obj):...
import datetime
if isinstance(obj, datetime.datetime):
return datetime.datetime.strftime(obj, '%Y-%m-%d %H:%M:%S')
def json_dump(obj):...
import json
from core.libs.playhouse.shortcuts import model_to_dict
return json.loads(json.dumps(model_to_dict(obj, recurse=False), default=
    default, separators=(', ', ': '), indent=1))
