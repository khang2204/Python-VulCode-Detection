import mimetypes
import os
from django.contrib.gis.db.models import GeometryField
from django.contrib.gis.db.models.functions import Envelope
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.functions import Cast
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from rest_framework import status, serializers, viewsets, filters, exceptions, permissions, parsers
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.views import APIView
from .common import get_and_check_project, get_tile_json
from app import models, scheduler, pending_actions
from nodeodm.models import ProcessingNode
def to_representation(self, obj):...
return obj.id
