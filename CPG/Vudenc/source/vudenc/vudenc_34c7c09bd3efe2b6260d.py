def get(self):...
xsrf_tool = XsrfTool()
user = users.get_current_user()
self.render('admin_delete_record.html', id=self.env.domain + '/person.',
    xsrf_token=xsrf_tool.generate_token(user.user_id(), 'admin_delete_record'))
