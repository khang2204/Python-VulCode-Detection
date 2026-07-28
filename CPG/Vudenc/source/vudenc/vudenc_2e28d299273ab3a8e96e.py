def get_url(urlname, group=None, args=None, kw=None):...
if group is None:
return reverse(urlname, args=args)
app = group._meta.app_label
urlconf = '.'.join([app, 'urls'])
url = reverse(urlname, urlconf, kwargs=kw)
return ''.join(['/', app, url])
