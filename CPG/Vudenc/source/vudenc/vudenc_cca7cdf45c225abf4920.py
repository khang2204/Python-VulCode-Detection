from .model import random_id
import subprocess
import json
import os
from .settings import settings
from .exceptions import NotFoundError, BadRequestError
def __init__(self, obj, readonly=False):...
self.id = random_id(obj.get('id'))
self.name = obj['name']
self.category = obj.get('category', 'Misc')
self.program = obj['program']
self.arguments = obj.get('arguments', [])
self.readonly = readonly
self.ui_properties = obj.get('ui_properties', None)
def to_map(self):...
return {'id': self.id, 'name': self.name, 'category': self.category,
    'program': self.program, 'arguments': self.arguments, 'readonly': self.
    readonly, 'ui_properties': self.ui_properties}
