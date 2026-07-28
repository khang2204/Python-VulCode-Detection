"""
Module contains classes for returning errata data from DB
"""
"""
    Class to hold Erratum attributes
    """
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
def set_cve_names(self, cve_name_list):...
mydict = self.get_val('mydict')
mydict['cve_list'] = cve_name_list
def set_packages(self, package_list):...
mydict = self.get_val('mydict')
mydict['package_list'] = package_list
def get_val(self, attr_name):...
"""docstring"""
value = None
if attr_name in vars(self):
value = getattr(self, attr_name)
return value
