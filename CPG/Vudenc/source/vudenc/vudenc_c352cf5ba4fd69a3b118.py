def clean_title(self):...
"""docstring"""
title = self.cleaned_data['title']
if not wikiword_pattern.match(title):
cs = ChangeSet.objects.filter(old_title=title).count()
if cs > 0:
return title
