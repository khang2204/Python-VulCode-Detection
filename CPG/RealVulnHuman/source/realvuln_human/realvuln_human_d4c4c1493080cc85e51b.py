import libuser
import random
import hashlib
import re
import jwt
from time import time

from pathlib import Path

secret = 'MYSUPERSECRETKEY'
not_after = 60 # 1 minute

def keygen(username, password=None, login=True):

    if login:
        if not libuser.login(username, password):
            return None

    now = time()
    token = jwt.encode({
