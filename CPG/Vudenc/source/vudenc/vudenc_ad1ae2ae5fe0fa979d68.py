def render_template(handler_object, file_name, template_values):...
user = users.get_current_user()
if user:
current_li = db.GqlQuery('SELECT * FROM LoginInformation WHERE user_id = :1',
    user.user_id()).get()
current_li = None
template_values['current_li'] = current_li
template_values['user'] = user
template_values['logout_url'] = users.create_logout_url('/')
template_values['login_url'] = users.create_login_url('/users/verify_user/')
template_values['is_admin'] = users.is_current_user_admin()
if user:
li = db.GqlQuery('SELECT * FROM LoginInformation WHERE user_id = :1', user.
    user_id()).get()
template = jinja_environment.get_template(file_name)
template_values['unread_messages'] = db.GqlQuery(
    'SELECT * FROM Message WHERE recipient_id = :1 AND read = :2', user.
    user_id(), False).count()
handler_object.response.out.write(template.render(template_values))
if li and not li.is_active:
file_name = '/users/inactive_notification.html'
