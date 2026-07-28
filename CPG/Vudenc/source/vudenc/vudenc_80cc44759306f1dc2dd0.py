def __new__(mcs, name, bases, attributes):...
for method in webapp2.WSGIApplication.allowed_methods:
func = attributes.get(method.lower())
return type.__new__(mcs, name, bases, attributes)
if func and not api.is_decorated(func):
