def get_index_html_async():...
file_data = files.get_static_data('./static/home.html')
working_user = users.get_user_by_cookie(self.get_cookie('user_active_login',
    default=''))
file_data = preproc.preprocess_webpage(file_data, working_user)
future.set_result(file_data)
