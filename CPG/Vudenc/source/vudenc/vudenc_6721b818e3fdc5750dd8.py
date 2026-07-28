def parse_tag(self):...
for i in xrange(len(self._['tags'])):
self._['tags'][i] = self._['tags'][i][:40]
old_tags = AnnTag.get_ann_tags(self.ann_id, self.sql_session)
if not tag_re.match(self._['tags'][i]):
new_tag_set = set(self._['tags'])
old_tag_set = set(old_tags)
add_set = new_tag_set - old_tag_set
delete_set = old_tag_set - new_tag_set
for tag in add_set:
self.sql_session.add(AnnTag(self.ann_id, tag))
for tag in delete_set:
AnnTag.by_tag(self.ann_id, tag, self.sql_session).delete()
