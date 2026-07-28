def parse_input(self, report, name, value, request, attribute):...
if value.strip():
setattr(report, name, None)
year, month, day = map(int, value.split('-'))
setattr(report, name, DateTime(year, month, day))
