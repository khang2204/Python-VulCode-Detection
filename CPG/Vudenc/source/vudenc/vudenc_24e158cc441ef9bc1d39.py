@BaseHandler.check_is_group_user('Announcement Manager')...
self.ann_id = ann_id if ann_id else ''
self._['id'] = self.ann_id
self._['title'] = self.get_argument('title', '')
self._['content'] = self.get_argument('content', '')
self.group = self.get_argument('group', '')
self._['is_private'] = bool(self.get_argument('is_private', ''))
self._['tags'] = self.get_arguments('tag')
self.attkeys = self.get_arguments('attachment')
if not self.check_ann():
self._['tmpatts'] = [att.to_dict() for att in self._['tmpatts']]
self._['author_name'] = self.current_user.name
return self.write(self._)
if self.ann_id:
Announce.by_id(self.ann_id, self.sql_session).update({'title': self._[
    'title'], 'content': self._['content'], 'author_group_name': self._[
    'author_group_name'], 'author_name': self._['author_name'],
    'is_private': self._['is_private']})
new_ann = Announce(**self._)
Record.add('update', self.ann_id, self.sql_session)
self.sql_session.add(new_ann)
self.parse_att()
self.sql_session.flush()
self.parse_tag()
self.sql_session.refresh(new_ann)
self.sql_session.commit()
self.ann_id = new_ann.id
self.write({'success': True, 'id': self.ann_id})
Record.add('new', self.ann_id, self.sql_session)
