from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.core.mail import send_mail
import datetime
import random
import string
import json
client = MongoClient()
db = client.freemail_database
ALPHABET = string.ascii_letters + string.digits
import settings
import os
SALT = os.environ.get('DJANGO_SALT')
import hashlib
def index(request):...
return render(request, 'index.html')
