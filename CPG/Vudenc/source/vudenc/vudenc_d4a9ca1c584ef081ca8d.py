from binance.client import Client
import configparser
import sqlite3
def getlist(option, sep=',', chars=None):...
"""docstring"""
return [chunk.strip(chars) for chunk in option.split(sep)]
