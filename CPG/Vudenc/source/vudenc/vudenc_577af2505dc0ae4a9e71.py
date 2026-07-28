def __log_traverse_one(self, path, attribute, source, target):...
if target is None:
mode = 'ADD'
if source is None:
data = '%s,None' % source
mode = 'REMOVE'
mode = 'UPDATE'
if not attribute is None:
data = 'None,%s' % target
data = '%s,%s' % (source, target)
parent = '(%s)' % path.parent
self.__logger.debug('%s ROOT (%s)' % (mode, data))
self.__logger.debug('%s%s %s.%s (%s)' % ('  ' * len(path), mode, parent,
    attribute.resource_attr, data))
