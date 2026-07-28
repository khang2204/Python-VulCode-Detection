import json
import logging
import os.path
import shutil
from glob import glob
from urllib.parse import quote
import aiohttp_jinja2
import jinja2
from aiohttp import web
from pyexiv2 import ImageMetadata
from natsort import natsorted
import settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger = logging.getLogger(__name__)
"""
    An image in your storage.

    Called `Item` to avoid clashing with PIL's `Image`.
    """
FORM = 'Iptc.Application2.Headline', 'Iptc.Application2.Caption'
"""A gallery item."""
def __init__(self, path):...
self.path = path
self.abspath = settings.STORAGE_DIR + path
self.meta = ImageMetadata(self.abspath)
self.meta.read()
def __str__(self):...
return os.path.basename(self.path)
