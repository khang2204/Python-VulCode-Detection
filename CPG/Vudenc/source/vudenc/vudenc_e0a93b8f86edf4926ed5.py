def account_info(remote, resp):...
"""docstring"""
account_info = dict(external_id=resp.get('orcid'), external_method='orcid')
return account_info
