def update_existing(self, dest_obj, context=None, ignore_fields=None):...
"""docstring"""
self.full_clean(ignore_fields)
mapping = registration.get_mapping(self.__class__, dest_obj.__class__)
return mapping(self, context).update(dest_obj, ignore_fields)
