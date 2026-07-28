from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ShortUrlForm, JustURLForm, CategoryModelForm, ManyURLSForm, JustULRUpdateForm, CategoryUpdateModelForm, CounterCountingForm
from .models import JustURL, Category, ClickTracking
from .utils import create_short_url, token_generator, generate_csv, get_client_ip, check_input_url
import re
def get(self, request, *args, **kwargs):...
form = ShortUrlForm()
return render(request, 'home.html', {'form': form})
