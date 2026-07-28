@classmethod...
"""docstring"""
hierarchy = hierarchy.lower()
class_name = cls.__name__.lower()
class_url = u'{0}/{1}/{2}'.format(base_url, hierarchy, cls.__name__.lower())
uuid_regex = ('[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}' +
    '-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
object_url = u'{0}/<regex("{1}"):uuid>'.format(class_url, uuid_regex)
flask.add_url_rule(class_url, u'_'.join([cls.__name__, 'get_objects']), cls
    .get_objects, methods=['GET'])
flask.add_url_rule(object_url, u'_'.join([cls.__name__, 'get_object']), cls
    .get_object, methods=['GET'])
flask.add_url_rule(object_url, u'_'.join([cls.__name__, 'put_object']), cls
    .put_object, methods=['PUT'])
flask.add_url_rule(class_url, u'_'.join([cls.__name__, 'create_object']),
    cls.create_object, methods=['POST'])
flask.add_url_rule(object_url, u'_'.join([cls.__name__, 'delete_object']),
    cls.delete_object, methods=['DELETE'])
