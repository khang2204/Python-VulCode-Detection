import base64
import binascii
import io
import json
import re
import time
import tornado
from bzs import files
from bzs import const
from bzs import users
from bzs import preproc
import os
def encode_str_to_hexed_b64(data):...
return binascii.b2a_hex(base64.b64encode(data.encode('utf-8'))).decode('utf-8')
