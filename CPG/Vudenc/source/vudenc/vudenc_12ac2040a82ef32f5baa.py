from twisted.internet.defer import inlineCallbacks, returnValue
from base import Query
"""
    Object representing an update query
    """
def __init__(self, model_class, values):...
super(UpdateQuery, self).__init__(model_class)
self.values = values
self.return_id = self.model_class._meta.primary_key
@inlineCallbacks...
query = self.database.generate_update(self)
if self.return_id:
result = yield self.database.runQuery(query)
yield self.database.runOperation(query)
if result and self.model_class._meta.primary_key:
returnValue(None)
returnValue(result[0][0])
