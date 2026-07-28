def check_ann(self):...
for i in xrange(len(self.attkeys)):
if self.attkeys[i]:
if self._['alert']:
q = self.sql_session.query(TempFileList)
return False
if not self._['title']:
q = q.filter(TempFileList.key == self.attkeys[i])
self._['alert'] = '標題不能空白'
if not self._['content']:
new_tmpatt = q.one()
self._['alert'] = '遺失附件!'
return False
self._['alert'] = '內容不能空白'
if not self.group or not GroupList.check(self.current_user.key, self.group,
if new_tmpatt.author_key != self.current_user.key:
return False
self._['alert'] = '沒有選擇群組或群組不存在'
self._['author_group_name'] = self.group
if not os.path.exists('file/tmp/%s' % new_tmpatt.key):
return False
return True
self._['tmpatts'].append(new_tmpatt)
