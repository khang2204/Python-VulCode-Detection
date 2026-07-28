def __init__(self, model_class, values):...
super(UpdateQuery, self).__init__(model_class)
self.values = values
self.return_id = self.model_class._meta.primary_key
