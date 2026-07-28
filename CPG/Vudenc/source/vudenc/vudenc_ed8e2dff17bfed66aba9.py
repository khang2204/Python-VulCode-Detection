def __call__(self, msg, arguments, errorSink=None):...
if arguments.strip():
return
if pytz is not None:
dt = datetime.now(pytz.UTC)
dt = datetime.utcnow()
if self._timezone is not None:
self.reply(msg, self._format_date(dt))
dt = dt.astimezone(self._timezone)
