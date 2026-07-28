def __init__(self, timezone, **kwargs):...
super().__init__(**kwargs)
if pytz is None:
logging.warn('Timezone support disabled, install pytz to enable.')
self._timezone = pytz.timezone(timezone)
self._timezone = None
