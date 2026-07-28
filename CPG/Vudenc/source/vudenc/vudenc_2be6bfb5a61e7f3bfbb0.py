from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
from .models import tweet
from .forms import SearchForm
from django.http import JsonResponse
from urllib.parse import urlparse
from http.client import HTTPSConnection
from datetime import datetime, timezone, timedelta
template_name = 'twitter/index.html'
context_object_name = 'tws'
paginate_by = 30
def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
search_form = SearchForm(self.request.GET)
context['search_form'] = search_form
count = self.object_list.count()
context['count'] = count
context['30_day_labels'] = self.thirty_day_labels()
context['30_day_data'] = self.thirty_day_data()
return context
