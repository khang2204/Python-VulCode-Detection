from flask import redirect, make_response
from random import randint
import redis
import uuid
import time
def initRedis_db():...
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
return r
