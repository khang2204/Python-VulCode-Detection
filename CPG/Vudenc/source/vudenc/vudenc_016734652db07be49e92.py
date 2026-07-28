from elasticsearch_dsl import FacetedSearch, TermsFacet
from elasticsearch_dsl.query import SimpleQueryString, Bool
"""Overwrite the initialization in order too meet our needs"""
def __init__(self, using, index, doc_types, model, fields=None, **kwargs):...
self.using = using
self.index = index
self.doc_types = doc_types
self._model = model
if fields:
self.fields = fields
super(RTDFacetedSearch, self).__init__(**kwargs)
fields = ['name^5', 'description']
facets = {'language': TermsFacet(field='language')}
facets = {'project': TermsFacet(field='project'), 'version': TermsFacet(
    field='version')}
def query(self, search, query):...
"""docstring"""
if query:
search = search.query(query)
return search
