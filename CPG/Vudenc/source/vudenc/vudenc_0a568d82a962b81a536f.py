@BaseHandler.check_is_group_user('Announcement Manager')...
if ann_id:
ann = Announce.by_id(ann_id, self.sql_session).scalar()
self._['user_groups'] = GroupList.get_user_groups(self.current_user.key,
    self.sql_session)
if not ann:
self.page_render(self._)
self._['ann_id'] = ann_id
self._['title'] = ann.title
self._['content'] = ann.content
self._['is_private'] = ann.is_private
atts = AttachmentList.by_ann_id(ann_id, self.sql_session).all()
self._['tags'] = AnnTag.get_ann_tags(ann_id, self.sql_session)
self._['atts'] = [att.to_dict() for att in atts]
if self.is_group_user(ann.author_group_name):
self._['group'] = ann.author_group_name
