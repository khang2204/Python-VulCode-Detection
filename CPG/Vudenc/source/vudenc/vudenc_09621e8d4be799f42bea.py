def __init__(self, model_class, values):...
super(InsertQuery, self).__init__(model_class)
self.values = values
self.on_conflict = self.model_class._meta.on_conflict
self.return_id = self.model_class._meta.primary_key
