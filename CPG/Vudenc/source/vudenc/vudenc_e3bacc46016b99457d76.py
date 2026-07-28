def make_input(version, report, attribute):...
"""docstring"""
name = attribute.key().name()
return ATTRIBUTE_TYPES[attribute.type].make_input(version, name, getattr(
    report, name, None), attribute)
