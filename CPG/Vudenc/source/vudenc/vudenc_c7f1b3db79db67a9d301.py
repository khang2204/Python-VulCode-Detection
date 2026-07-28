import base64
import collections
import datetime
import hmac
import json
import os
import re
import subprocess
import time
import psycopg2
import requests
import unidiff
import yaml
from flask import abort
def update_users(repository):...
"""docstring"""
if os.environ.get('OVER_HEROKU', False) is not False:
query = ("INSERT INTO Users (repository, created_at) VALUES ('{}', now());"
    .format(repository))
def follow_user(user):...
cursor.execute(query)
conn.rollback()
"""docstring"""
conn.commit()
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN'],
    'Content-Length': '0'}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
url = 'https://api.github.com/user/following/{}'
url = url.format(user)
r = requests.put(url, headers=headers, auth=auth)
def update_dict(base, head):...
"""docstring"""
for key, value in head.items():
if isinstance(base, collections.Mapping):
return base
if isinstance(value, collections.Mapping):
base = {key: head[key]}
base[key] = update_dict(base.get(key, {}), value)
base[key] = head[key]
