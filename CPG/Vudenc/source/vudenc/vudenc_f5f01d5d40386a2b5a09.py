from twisted.internet.defer import inlineCallbacks, returnValue
from base import Query
"""
    Object representing an insert query
    """
def __init__(self, model_class, values):...
super(InsertQuery, self).__init__(model_class)
self.values = values
self.on_conflict = self.model_class._meta.on_conflict
self.return_id = self.model_class._meta.primary_key
@inlineCallbacks...
query = self.database.generate_insert(self)
if self.return_id:
result = yield self.database.runQuery(query)
yield self.database.runOperation(query)
if result and self.model_class._meta.primary_key:
returnValue(None)
returnValue(result[0][0])
