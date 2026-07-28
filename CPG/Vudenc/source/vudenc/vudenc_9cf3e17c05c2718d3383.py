from datetime import datetime
from django.conf import settings
from django.core.cache import cache
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponseNotAllowed, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from wiki.forms import ArticleForm
from wiki.models import Article, ChangeSet, dmp
from wiki.utils import get_ct
from django.contrib.auth.decorators import login_required
from wl_utils import get_real_ip
import re
WIKI_LOCK_DURATION = settings.WIKI_LOCK_DURATION
WIKI_LOCK_DURATION = 15
from notification import models as notification
notification = None
ALL_ARTICLES = Article.objects.all()
ALL_CHANGES = ChangeSet.objects.all()
def get_articles_by_group(article_qs, group_slug=None, group_slug_field=...
group = None
if group_slug is not None:
group = get_object_or_404(group_qs, **{group_slug_field: group_slug})
return article_qs, group
article_qs = article_qs.filter(content_type=get_ct(group), object_id=group.id)
