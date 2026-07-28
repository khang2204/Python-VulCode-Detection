def __init__(self, title, request, message_template=None):...
self.title = title
self.user_ip = get_real_ip(request)
self.created_at = datetime.now()
if message_template is None:
message_template = (
    'Possible edit conflict: another user started editing this article at %s')
self.message_template = message_template
cache.set(title, self, WIKI_LOCK_DURATION * 60)
