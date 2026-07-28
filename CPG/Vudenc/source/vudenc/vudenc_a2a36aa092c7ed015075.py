__author__ = 'zkqiang'
__zhihu__ = 'https://www.zhihu.com/people/z-kqiang'
__github__ = 'https://github.com/zkqiang/Zhihu-Login'
import requests
import time
import re
import base64
import hmac
import hashlib
import json
import matplotlib.pyplot as plt
from http import cookiejar
from PIL import Image
HEADERS = {'Connection': 'keep-alive', 'Host': 'www.zhihu.com', 'Referer':
    'https://www.zhihu.com/', 'User-Agent':
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
    }
LOGIN_URL = 'https://www.zhihu.com/signup'
LOGIN_API = 'https://www.zhihu.com/api/v3/oauth/sign_in'
FORM_DATA = {'client_id': 'c3cef7c66a1843f8b3a9e6a1e3160e20', 'grant_type':
    'password', 'source': 'com.zhihu.web', 'username': '', 'password': '',
    'lang': 'en', 'ref_source': 'homepage'}
def __init__(self):...
self.login_url = LOGIN_URL
self.login_api = LOGIN_API
self.login_data = FORM_DATA.copy()
self.session = requests.session()
self.session.headers = HEADERS.copy()
self.session.cookies = cookiejar.LWPCookieJar(filename='./cookies.txt')
def login(self, username=None, password=None, load_cookies=True):...
"""docstring"""
if load_cookies and self.load_cookies():
if self.check_login():
headers = self.session.headers.copy()
return True
headers.update({'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    'X-Xsrftoken': self._get_token()})
username, password = self._check_user_pass(username, password)
self.login_data.update({'username': username, 'password': password})
timestamp = str(int(time.time() * 1000))
self.login_data.update({'captcha': self._get_captcha(headers), 'timestamp':
    timestamp, 'signature': self._get_signature(timestamp)})
resp = self.session.post(self.login_api, data=self.login_data, headers=headers)
if 'error' in resp.text:
print(re.findall('"message":"(.+?)"', resp.text)[0])
if self.check_login():
print('登录失败')
return True
return False
