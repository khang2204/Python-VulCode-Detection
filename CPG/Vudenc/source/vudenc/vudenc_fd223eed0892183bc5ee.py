def _check_user_pass(self, username, password):...
"""docstring"""
if username is None:
username = self.login_data.get('username')
if '+86' not in username:
if not username:
username = '+86' + username
if password is None:
username = input('请输入手机号：')
password = self.login_data.get('password')
return username, password
if not password:
password = input('请输入密码：')
