def parse_input(self, report, name, value, request, attribute):...
if value:
value = value == 'TRUE'
value = None
setattr(report, name, value)
