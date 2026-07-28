def _transform_decimal(self, value):...
context = decimal.Context(prec=self.max_digits)
return value.quantize(decimal.Decimal(1), context=context
    ) if value == value.to_integral() else value.normalize(context)
