import vim
import requests
import urlparse
from retries import retries
from requests_futures.sessions import FuturesSession
from ycm.unsafe_thread_pool_executor import UnsafeThreadPoolExecutor
from ycm import vimsupport
from ycm.utils import ToUtf8Json
from ycm.server.responses import ServerError, UnknownExtraConf
_HEADERS = {'content-type': 'application/json'}
_EXECUTOR = UnsafeThreadPoolExecutor(max_workers=30)
_DEFAULT_TIMEOUT_SEC = 30
def __init__(self):...
def Start(self):...
def Done(self):...
return True
