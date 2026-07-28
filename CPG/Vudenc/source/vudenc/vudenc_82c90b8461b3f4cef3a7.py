@handler('request_value_changed')...
if value.handled:
return
req, res = value.event.args[:2]
if value.result and not value.errors:
res.body = value.value
if value.promise:
self.fire(response(res))
value.event.notify = True
self.fire(httperror(req, res, error=value.value))
