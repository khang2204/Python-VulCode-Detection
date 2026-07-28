def parse_att(self):...
for att in self._['tmpatts']:
os.makedirs('file/%s' % att.key)
os.rename('file/tmp/%s' % att.key, 'file/%s/%s' % (att.key, att.filename))
new_att = AttachmentList(key=att.key, ann_id=self.ann_id, content_type=att.
    content_type, filename=att.filename)
self.sql_session.add(new_att)
TempFileList.by_key(att.key, self.sql_session).delete()
