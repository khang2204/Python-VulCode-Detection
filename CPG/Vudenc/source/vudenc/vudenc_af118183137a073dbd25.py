def make_logout_url(dest_url):...
"""docstring"""
return '/logout?' + urllib.parse.urlencode({'csrf_token': form.
    generate_csrf_token(), 'dest': dest_url})
