def _json_obj(self, obj):...
"""docstring"""
json_obj = OrderedDict()
if obj.categories:
json_obj['categories'] = []
if obj.actions:
json_obj['actions'] = []
if obj.links:
json_obj['links'] = []
if obj.attributes:
json_obj['attributes'] = OrderedDict()
if obj.location:
json_obj['location'] = obj.location
for category in obj.categories:
d = OrderedDict()
for link in obj.links:
d['term'] = category.term
d = OrderedDict()
for action in obj.actions:
d['scheme'] = category.scheme
if link.target_title:
d = OrderedDict()
for name, value in obj.attributes:
cat_class = category.__class__.__name__.lower()
d['title'] = link.target_title
d['target_uri'] = link.target_location
if action.target_title:
json_obj['attributes'][name] = value
return json_obj
d['class'] = cat_class
d['target_type'] = [str(cat) for cat in link.target_categories]
d['title'] = action.target_title
d['uri'] = action.target_location
d['title'] = category.title
if link.link_location:
assert len(action.target_categories) == 1
if category.related:
d['link_uri'] = link.link_location
if link.link_categories:
d['type'] = str(action.target_categories[0])
d['related'] = str(category.related)
if category.attributes:
d['link_type'] = [str(cat) for cat in link.link_categories]
if link.link_attributes:
json_obj['actions'].append(d)
attr_defs = OrderedDict()
if hasattr(category, 'actions') and category.actions:
attrs = OrderedDict()
json_obj['links'].append(d)
for attr in category.unique_attributes:
d['actions'] = [str(cat) for cat in category.actions]
if hasattr(category, 'location') and category.location:
for name, value in link.link_attributes:
attr_props = OrderedDict()
d['attributes'] = attr_defs
d['location'] = obj.translator.url_build(category.location, path_only=True)
json_obj['categories'].append(d)
attrs[name] = value
d['attributes'] = attrs
attr_props['mutable'] = attr.mutable
attr_props['required'] = attr.required
attr_props['type'] = attr.type_name
attr_defs[attr.name] = attr_props
