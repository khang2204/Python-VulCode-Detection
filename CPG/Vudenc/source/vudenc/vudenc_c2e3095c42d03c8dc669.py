"""
Created on Sun Jan 14 21:55:57 2018

@author: adam
"""
import os
import warnings
import sqlite3
import datetime
from collections.abc import Iterable
from ast import literal_eval
import numpy as np
import pandas as pd
from .core import DATA_DIRE
""" `There was an accident with a contraceptive and a time machine.`
    """
def db_path(name):...
"""docstring"""
fil = os.path.join(DATA_DIRE, name + '.db')
return fil
