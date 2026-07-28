def scan(securedrop: DirectoryEntry, commit=False) ->ScanResult:...
"""docstring"""
securedrop_domain = url_to_domain(securedrop.landing_page_url)
pshtt_results = inspect_domains([securedrop_domain], {'timeout': 10})
result = pshtt_data_to_result(securedrop, pshtt_results[0])
if commit:
result.securedrop = securedrop
return result
result.save()
