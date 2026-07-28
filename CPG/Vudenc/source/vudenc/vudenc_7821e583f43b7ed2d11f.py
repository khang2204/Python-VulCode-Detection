def backlinks(request, title):...
"""docstring"""
this_article = Article.objects.get(title=title)
changesets = this_article.changeset_set.all()
old_titles = []
for cs in changesets:
if cs.old_title and cs.old_title != title and cs.old_title not in old_titles:
m = re.match('(!?)(\\b[A-Z][a-z]+[A-Z]\\w+\\b)', title)
old_titles.append(cs.old_title)
if m:
search_title = re.compile('%s' % title)
search_title = re.compile('\\/%s\\)' % title)
found_old_links = []
found_links = []
articles_all = Article.objects.all().exclude(title=title)
for article in articles_all:
match = search_title.search(article.content)
context = {'found_links': found_links, 'found_old_links': found_old_links,
    'name': title}
if match:
return render_to_response('wiki/backlinks.html', context, context_instance=
    RequestContext(request))
found_links.append({'title': article.title})
for old_title in old_titles:
if old_title in article.content:
found_old_links.append({'old_title': old_title, 'title': article.title})
