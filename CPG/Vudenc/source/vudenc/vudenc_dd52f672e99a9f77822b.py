def parse_input(self, report, name, value, request, attribute):...
if value:
value = int(float(value))
value = None
setattr(report, name, value)
