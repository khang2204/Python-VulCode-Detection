from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import logging
from datetime import datetime
import peewee
import smtplib
import tornado.web
import db
import handlers
import settings
def build_dataset_structure(dataset_version, user=None, dataset=None):...
if dataset is None:
dataset = dataset_version.dataset
r = db.build_dict_from_row(dataset)
r['version'] = db.build_dict_from_row(dataset_version)
r['version']['available_from'] = r['version']['available_from'].strftime(
    '%Y-%m-%d')
r['has_image'] = dataset.has_image()
if user:
r['is_admin'] = user.is_admin(dataset)
return r
if user.has_access(dataset):
r['authorization_level'] = 'has_access'
if user.has_requested_access(dataset):
r['authorization_level'] = 'has_requested_access'
r['authorization_level'] = 'no_access'
