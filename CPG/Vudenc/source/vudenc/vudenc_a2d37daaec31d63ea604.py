def parse_input(self, report, name, value, request, attribute):...
contact = request.get(name + '.name', '') + '|' + request.get(name +
    '.phone', '') + '|' + request.get(name + '.email', '')
contact = contact != '||' and contact or ''
setattr(report, name, contact)
