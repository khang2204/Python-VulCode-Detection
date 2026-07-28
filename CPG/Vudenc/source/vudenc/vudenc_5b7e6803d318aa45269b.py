def __init__(self, using, index, doc_types, model, fields=None, **kwargs):...
self.using = using
self.index = index
self.doc_types = doc_types
self._model = model
if fields:
self.fields = fields
super(RTDFacetedSearch, self).__init__(**kwargs)
