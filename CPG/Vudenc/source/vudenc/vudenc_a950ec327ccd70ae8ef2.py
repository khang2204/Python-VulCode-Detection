import unittest
from ... import create_app
app = create_app('config.TestConfig')
"""A base test case."""
def create_app(self):...
app.config.from_object('config.TestConfig')
return app
