@BaseHandler.check_is_group_user('Announcement Manager')...
if not ann_id:
if not Announce.by_id(ann_id, self.sql_session).scalar():
q = AttachmentList.by_ann_id(ann_id, self.sql_session)
old_atts = q.all()
for old_att in old_atts:
shutil.rmtree('file/%s' % old_att.key)
q.delete()
Announce.by_id(ann_id, self.sql_session).delete()
self.write({'success': True})
