def runPlugin(name):...
module = __import__(name.replace('\r', ''))
class_ = getattr(module, name.replace('\r', ''))
instance = class_()
return callMethod(instance, 'fetch') + LINEBREAK + '.' + LINEBREAK
