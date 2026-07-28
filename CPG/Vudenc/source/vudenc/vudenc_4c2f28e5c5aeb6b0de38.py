def _build_fast_url(term, index):...
url = '%s?query=%s&queryIndex=%s' % (settings.FAST_LOOKUP_BASE_URL, urllib.
    parse.quote(term), index)
url = '%s&queryReturn=%s&suggest=autoSubject' % (url, urllib.parse.quote(
    'idroot,auth,type,%s' % index))
return url
