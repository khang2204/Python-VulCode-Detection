def is_group_user(self, group):...
if not self.current_user:
return False
if self.current_user.admin:
return True
group = GroupList.check(self.current_user.key, group, self.sql_session)
return bool(group)
