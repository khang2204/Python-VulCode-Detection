def calculate_tag_count(self, tag):...
"""docstring"""
if self.counter['tag'] != tag.pk:
if tag.pk == self.counter['tag']:
self.counter = self.test_tags.__next__()
return 0
return self.counter[self.key]
return 0
