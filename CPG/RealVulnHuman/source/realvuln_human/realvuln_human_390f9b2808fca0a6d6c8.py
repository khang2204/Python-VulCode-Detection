import os
from decimal import Decimal
from datetime import datetime, timedelta
from sqlalchemy import event
from sqlalchemy.engine import Engine
import sqlite3

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vulnerable_bank.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {
        'timeout': 10,  # Set SQLite timeout to 10 seconds
        'check_same_thread': False,  # Allow access from multiple threads
        'isolation_level': None,  # Use autocommit mode
    },
    'poolclass': None,  # Disable connection pooling for SQLite
    'pool_pre_ping': True,  # Check connection validity before using from pool
