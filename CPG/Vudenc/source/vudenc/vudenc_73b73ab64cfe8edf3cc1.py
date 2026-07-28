def zmi_body_class(self, *args, **kwargs):...
request = self.REQUEST
l = ['zmi']
l.append(request['lang'])
l.extend(map(lambda x: kwargs[x], kwargs.keys()))
l.append(self.meta_id)
internal_dict = self.attr('internal_dict')
if isinstance(internal_dict, dict) and internal_dict.get('css_classes', None):
l.extend(internal_dict['css_classes'])
l.extend(request['AUTHENTICATED_USER'].getRolesInContext(self))
return ' '.join(l)
