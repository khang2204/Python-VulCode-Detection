@staticmethod...
tags = ['sup', 'i', 'span']
return getattr(element, 'name', None) == 'a' and getattr(element.parent,
    'name', None) not in tags and not element.has_attr('style')
