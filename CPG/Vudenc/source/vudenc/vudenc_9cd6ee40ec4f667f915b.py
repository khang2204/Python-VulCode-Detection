def validate(self, value, model_instance):...
super().validate(value, model_instance)
options = {'cls': self.encoder} if self.encoder else {}
json.dumps(value, **options)
