def __init__(self, **ka):...
self.type = ka['type']
if 'vals' in ka:
formatting = list(map(html_escape, ka['vals']))
self.message = ka['message']
self.message = ka['message'].format(*formatting)
if self.type not in ('success', 'info') and 'no_sure' not in ka:
self.message += '<p><b>Are you sure you want to do this?</b></p>'
if self.type in self.status_types:
self.icon = self.status_types[self.type]
self.confirm = ka.get('yes', None)
self.deny = ka.get('no', None)
self.action = ka.get('action', None)
self.url = ka.get('url', None)
self.message_list = ka.get('message_list', None)
self.close = ka.get('close', True)
