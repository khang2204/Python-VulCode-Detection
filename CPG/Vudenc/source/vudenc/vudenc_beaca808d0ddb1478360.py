"""This module contains the device class and context manager"""
import abc
import logging
logging.getLogger()
"""Metaclass that allows derived classes to dynamically instantiate
    new objects based on undefined methods. The dynamic methods pass their arguments
    directly to __init__ of the inheriting class."""
def __getattr__(cls, name):...
"""docstring"""
def new_object(*args, **kwargs):...
"""docstring"""
return cls(name, *args, **kwargs)
