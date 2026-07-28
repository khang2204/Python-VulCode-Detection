import hashlib
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.urls import reverse
from django.template import RequestContext
from django.shortcuts import Http404, redirect, render, render_to_response
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView, FormMixin
from markdown import markdown
from .models import Article, Category, Comment
model = Article
fields = ['title', 'category', 'content']
model = Comment
fields = ['content']
model = User
template_name = 'user.html'
def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
context['articles'] = self.object.article_set.all()
context['form'] = CommentForm()
return context
