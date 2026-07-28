def __init__(self, id, name, synopsis, severity, description, solution,...
setattr(self, 'name', name)
setattr(self, 'id', id)
mydict = {}
mydict['type'] = None
mydict['issued'] = str(issued)
mydict['synopsis'] = synopsis
mydict['description'] = description
mydict['solution'] = solution
mydict['severity'] = severity
mydict['summary'] = None
mydict['updated'] = str(updated)
mydict['url'] = 'https://access.redhat.com/errata/%s' % name
mydict['bugzilla_list'] = []
mydict['cve_list'] = []
mydict['package_list'] = []
mydict['reference_list'] = []
setattr(self, 'mydict', mydict)
