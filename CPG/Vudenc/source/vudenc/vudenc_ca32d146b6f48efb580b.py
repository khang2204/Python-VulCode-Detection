def value_from_object(self, obj):...
value = super().value_from_object(obj)
if isinstance(value, decimal.Decimal):
return self._transform_decimal(value)
return value
