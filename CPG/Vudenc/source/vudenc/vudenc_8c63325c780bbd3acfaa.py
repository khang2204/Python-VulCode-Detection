def parse_input(self, report, name, value, request, attribute):...
if value:
value = float(value)
value = None
setattr(report, name, value)
