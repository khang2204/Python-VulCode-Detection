def display_icon(self, REQUEST, meta_type=None, key='icon', zpt=None):...
if meta_type is None:
return self.icon
return self.aq_parent.display_icon(REQUEST, meta_type, key, zpt)
