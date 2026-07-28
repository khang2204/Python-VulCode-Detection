def parse_input(report, request, attribute):...
"""docstring"""
name = attribute.key().name()
return ATTRIBUTE_TYPES[attribute.type].parse_input(report, name, request.
    get(name, None), request, attribute)
