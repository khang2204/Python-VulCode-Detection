def is_active(self):...
if self.field_name in self.query_params:
selected_value = self.query_params[self.field_name]
if self.value is None:
if type(selected_value) == list:
return True
return False
selected_value = selected_value[0]
if selected_value == self.value:
return True
