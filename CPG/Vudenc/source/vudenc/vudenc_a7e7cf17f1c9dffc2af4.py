import re
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from wiki.models import Article
from wiki.models import ChangeSet
from wiki.templatetags.wiki_extras import WIKI_WORD_RE
wikiword_pattern = re.compile('^' + WIKI_WORD_RE + '$')
summary = forms.CharField(widget=forms.Textarea)
comment = forms.CharField(required=False)
user_ip = forms.CharField(widget=forms.HiddenInput)
content_type = forms.ModelChoiceField(queryset=ContentType.objects.all(),
    required=False, widget=forms.HiddenInput)
object_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
action = forms.CharField(widget=forms.HiddenInput)
model = Article
exclude = 'creator', 'creator_ip', 'group', 'created_at', 'last_update'
def clean_title(self):...
"""docstring"""
title = self.cleaned_data['title']
if not wikiword_pattern.match(title):
cs = ChangeSet.objects.filter(old_title=title).count()
if cs > 0:
return title
