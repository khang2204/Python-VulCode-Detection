import asyncio, base64, bcrypt, time, string
from aiohttp import web
from cryptography import fernet
from aiohttp_session import setup as session_setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from psycopg2 import IntegrityError
import database
import mazemap
HTML_base = (
    """
<!doctype html>
<html>
<title>Toilet Finder</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

{text}

</html>
"""
    [1:-1])
def handle_html(func):...
async def ret(*args, **kwargs):...
session = await get_session(args[0])
if 'uname' in session and 'ignore_timeout' not in session:
t = time.time()
session['visit_time'] = time.time()
prev = session['visit_time']
text = await func(*args, **kwargs)
if t - prev > handle_html.timeout:
out = web.Response(content_type='text/html', text=HTML_base.format(text=text))
session['visit_time'] = t
return out
