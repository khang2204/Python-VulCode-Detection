def default(self, obj):...
if isinstance(obj, ndb.Model):
dict_obj = obj.to_dict()
if isinstance(obj, datetime.datetime):
dict_obj['id'] = obj.key.id()
return int((obj - self._EPOCH).total_seconds())
if hasattr(obj, 'to_dict'):
return dict_obj
return obj.to_dict()
if isinstance(obj, cgi.FieldStorage):
return str(obj)
