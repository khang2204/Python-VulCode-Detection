def render(self, path, values=None, status=200):...
"""docstring"""
if values is None:
values = {}
values['menu_items'] = _MENU_ITEMS
values['is_oss_fuzz'] = utils.is_oss_fuzz()
values['is_development'] = environment.is_running_on_app_engine_development()
values['is_logged_in'] = bool(helpers.get_user_email())
values['ga_tracking_id'] = local_config.GAEConfig().get('ga_tracking_id'
    ) if not auth.is_current_user_admin() else None
if values['is_logged_in']:
values['switch_account_url'] = make_login_url(self.request.url)
template = _JINJA_ENVIRONMENT.get_template(path)
values['logout_url'] = make_logout_url(dest_url=self.request.url)
self._add_security_response_headers()
self.response.headers['Content-Type'] = 'text/html'
self.response.out.write(template.render(values))
self.response.set_status(status)
