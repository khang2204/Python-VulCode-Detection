@auth.require(acl.is_ereporter2_editor)...
to_delete = self.request.get('to_delete')
if to_delete:
ndb.Key(models.ErrorReportingMonitoring, to_delete).delete()
mute_type = self.request.get('mute_type')
self.get()
error = None
if mute_type in ('exception_type', 'signature'):
error = self.request.get(mute_type)
if not error:
self.abort(400)
silenced = self.request.get('silenced')
silenced_until = self.request.get('silenced_until')
if silenced_until == 'T':
silenced_until = ''
threshold = self.request.get('threshold')
key = models.ErrorReportingMonitoring.error_to_key(error)
if not silenced and not silenced_until and not threshold:
key.delete()
item = models.ErrorReportingMonitoring(key=key, error=error)
if silenced:
item.silenced = True
if silenced_until:
item.silenced_until = datetime.datetime.strptime(silenced_until,
    '%Y-%m-%dT%H:%M')
if threshold:
item.threshold = int(threshold)
item.put()
