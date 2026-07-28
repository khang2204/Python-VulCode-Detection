import re
import typing
from urllib.parse import urlparse
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from lib.forms import ModelFormWithSubmit
from projects.project_models import Project
from .source_models import FileSource, GithubSource, Source
FILE_TYPES = [('text/dar', 'Dar'), ('text/dockerfile', 'Dockerfile'), (
    'text/ipynb', 'Jupyter Notebook'), ('text/rmarkdown', 'RMarkdown')]
def validate_unique_project_path(project: Project, path: str,...
"""docstring"""
existing_sources = FileSource.objects.filter(project=project, path=path)
if existing_source_pk:
existing_sources = existing_sources.exclude(pk=existing_source_pk)
if len(existing_sources):
type = forms.ChoiceField(choices=FILE_TYPES)
path = forms.RegexField(regex='^[^/][A-Za-z\\-/\\.]+[^/]$', widget=forms.
    TextInput, error_messages={'invalid':
    'The path must not contain spaces, or start or end with a /'})
model = FileSource
fields = 'path',
widgets = {'type': forms.Select(), 'path': forms.TextInput()}
def clean(self):...
validate_unique_project_path(self.initial['project'], self.cleaned_data['path']
    )
return super().clean()
