from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
from .models import Event, Attribute, Org, Tag, Object, ObjectReference
from .forms import EventSearchForm, AttributeSearchForm
from datetime import datetime, timezone, timedelta
model = Event
template_name = 'threat/event_list.html'
context_object_name = 'events'
paginate_by = 30
def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
context['count'] = self.object_list.count()
context['alltag'] = Tag.objects.order_by('id')
taglist = self.request.GET.getlist('tag')
context['tags'] = Tag.objects.filter(id__in=taglist)
search_form = EventSearchForm(self.request.GET)
context['search_form'] = search_form
context['30_day_labels'] = self.thirty_day_labels()
context['30_day_data'] = self.thirty_day_data()
return context
