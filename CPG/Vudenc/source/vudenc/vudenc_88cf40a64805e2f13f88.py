def get_myebay_selling_request(page):...
"""docstring"""
api_trading = Trading(config_file=PATH_TO_YAML, warnings=True, timeout=20)
print(e)
return products
api_request = {'ActiveList': {'Include': True, 'Pagination': {
    'EntriesPerPage': 100, 'PageNumber': page}, 'IncludeWatchCount': True},
    'DetailLevel': 'ReturnAll'}
print(e.response.dict())
api_trading.execute('GetMyeBaySelling', api_request)
products = api_trading.response.dict()
