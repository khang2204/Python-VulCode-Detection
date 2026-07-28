def cache_old_content(self):...
if self.instance.id is None:
self.old_title = self.old_content = self.old_markup = ''
self.old_title = self.instance.title
self.is_new = True
self.old_content = self.instance.content
self.old_markup = self.instance.markup
self.is_new = False
