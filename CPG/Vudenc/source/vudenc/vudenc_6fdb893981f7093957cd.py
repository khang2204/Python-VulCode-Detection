@decorators.require_cronjob...
old_cutoff = utils.utcnow() - on_error.ERROR_TIME_TO_LIVE
items = models.Error.query(models.Error.created_ts < old_cutoff,
    default_options=ndb.QueryOptions(keys_only=True))
out = len(ndb.delete_multi(items))
self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
self.response.write(str(out))
