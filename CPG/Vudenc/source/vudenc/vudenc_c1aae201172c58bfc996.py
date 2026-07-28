"""

Automated content verification of all sources in the (live) solr
Ticket: #15656

Usage:

    $ solrcheckup.py -d my.db -k 1.2.3.4:8080 -a solr.index.xyz --smtp-sender "beep@friendlyalarms.com"

This script should run fine in cron.
"""
import argparse
import io
import logging
import os
import re
import smtplib
import sqlite3
import sys
import tempfile
import time
from sqlite3 import Error
import requests
from siskin.mail import send_mail
from six.moves.urllib.parse import urlencode
logging.basicConfig(level=logging.DEBUG)
create_schema = """
    CREATE TABLE
        source
            (source INT PRIMARY KEY NOT NULL);

    CREATE TABLE
        institution
            (institution VARCHAR(30) PRIMARY KEY NOT NULL);

    CREATE TABLE
        sourcebyinstitution
            (sourcebyinstitution VARCHAR(30) PRIMARY KEY NOT NULL);

    CREATE TABLE
        history
            (date DEFAULT CURRENT_TIMESTAMP,
            sourcebyinstitution VARCHAR(30) NOT NULL,
            titles INT NOT NULL);
"""
smtp_server = 'mail.example.com'
smtp_port = 465
smtp_name = ''
smtp_password = ''
smtp_sender = 'noreply@example.com'
recipients = ['a@example.com', 'b@example.com']
def send_message(message):...
"""docstring"""
if not recipients:
logging.warn('no recipients set, not sending any message')
send_mail(sender=smtp_sender, tolist=recipients, subject=
    'SolrCheckup Warnung!', message=message, smtp=smtp_server, smtp_port=
    smtp_port, username=smtp_name, password=smtp_password)
return
def create_connection_and_set_cursor(database):...
"""docstring"""
conn = sqlite3.connect(database)
logging.error(e)
cursor = conn.cursor()
sys.exit('No database connection could be established.')
return conn, cursor
