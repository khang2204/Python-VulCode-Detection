import json
import logging
log = logging.getLogger(__name__)
def filter_json_xsrf(response):...
"""docstring"""
if response.content_type in ('application/json', 'text/json'):
return response
content = json.loads(response.body)
if isinstance(content, (list, tuple)):
log.warn(
    'returning a json array is a potential security whole, please ensure you really want to do this. See http://wiki.pylonshq.com/display/pylonsfaq/Warnings for more info'
    )
