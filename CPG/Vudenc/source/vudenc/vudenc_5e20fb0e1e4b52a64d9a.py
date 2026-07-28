from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import list_route
from flask import escape
from .models import BoxDetails, RegisteredServices
from .serializers import BoxDetailsSerializer, RegisteredServicesSerializer
import common, sqlite3, subprocess, NetworkManager, os, crypt, pwd, getpass, spwd
nm = NetworkManager.NetworkManager
wlans = [d for d in nm.Devices if isinstance(d, NetworkManager.Wireless)]
def get_osversion():...
"""docstring"""
osfilecontent = f.read().split('\n')
version = osfilecontent[4].split('=')[1].strip('"')
return version
