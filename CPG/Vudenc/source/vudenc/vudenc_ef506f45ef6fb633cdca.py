def safe_redirect(url):...
url_unquoted = urllib.parse.unquote_plus(url)
if url_unquoted.startswith(BASE_URL + '/'):
redirect(url)
redirect(BASE_URL)
