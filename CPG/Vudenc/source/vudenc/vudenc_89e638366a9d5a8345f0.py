import re
from flask import request
"""
        Stack data structure will not insert
        equal sequential data
    """
def __init__(self, list=None, size=5):...
self.size = size
self.data = list or []
def push(self, item):...
if self.data:
if item != self.data[len(self.data) - 1]:
self.data.append(item)
self.data.append(item)
if len(self.data) > self.size:
self.data.pop(0)
def pop(self):...
if len(self.data) == 0:
return None
return self.data.pop(len(self.data) - 1)
