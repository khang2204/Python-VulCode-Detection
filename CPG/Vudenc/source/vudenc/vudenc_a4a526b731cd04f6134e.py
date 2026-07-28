def __init__(self, user_id, leap_home):...
self._user_id = user_id
self._leap_home = leap_home
self._uuid = str(uuid.uuid4())
self._mail_address = '%s@pixelated.org' % user_id
self._soledad = None
self._services = None
