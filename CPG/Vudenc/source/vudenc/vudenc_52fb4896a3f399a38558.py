def validate_subdomain(url):...
"""docstring"""
parsed_domain = tldextract.extract(url)
return parsed_domain.subdomain not in ('', 'www')
