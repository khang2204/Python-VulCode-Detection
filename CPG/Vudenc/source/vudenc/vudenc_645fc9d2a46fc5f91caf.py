def to_doc(self, response):...
"""docstring"""
return scrape.Document(content_bytes=response.content, url=None, status=
    response.status_code, message=None, headers=response, charset=const.
    CHARSET_UTF8)
