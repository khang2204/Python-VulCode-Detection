@inlineCallbacks...
query = self.database.generate_update(self)
if self.return_id:
result = yield self.database.runQuery(query)
yield self.database.runOperation(query)
if result and self.model_class._meta.primary_key:
returnValue(None)
returnValue(result[0][0])
