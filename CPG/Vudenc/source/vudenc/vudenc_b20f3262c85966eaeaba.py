"""
Controller classes, handling actions required for archival
"""
import time, tempfile, asyncio, json, os, shutil, signal
from itertools import islice
from datetime import datetime
from operator import attrgetter
from abc import ABC, abstractmethod
from yarl import URL
from . import behavior as cbehavior
from .browser import SiteLoader, RequestResponsePair, PageIdle, FrameNavigated
from .util import getFormattedViewportMetrics, getSoftwareInfo
from .behavior import ExtractLinksEvent
__slots__ = 'idleTimeout', 'timeout', 'insecure'
def __init__(self, idleTimeout=2, timeout=10, insecure=False):...
self.idleTimeout = idleTimeout
self.timeout = timeout
self.insecure = insecure
def toDict(self):...
return dict(idleTimeout=self.idleTimeout, timeout=self.timeout, insecure=
    self.insecure)
