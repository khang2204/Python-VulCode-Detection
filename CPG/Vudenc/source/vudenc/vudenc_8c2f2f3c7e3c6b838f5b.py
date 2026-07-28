from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q, Count
from .models import tweet, Hunt
from .forms import HuntForm
import csv
from io import StringIO, BytesIO
from codecs import BOM_UTF8
from pytz import timezone
from django.http import JsonResponse
from urllib.parse import urlparse
from http.client import HTTPSConnection
template_name = 'twitter_hunter/index.html'
context_object_name = 'hts'
paginate_by = 30
def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
return context
