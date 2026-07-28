def get_template_namespace(self):...
_ = super(BaseHandler, self).get_template_namespace()
_['css_urls'] = self.assets['css_all'].urls()
_['js_urls'] = self.assets['js_all'].urls()
_['system_name'] = options.system_name
_['SERVER_DEBUG'] = options.server_debug
_['ip'] = self.request.remote_ip
_['system_version'] = system_version
_['_host'] = self.request.host
_['_protocol'] = self.request.protocol
if self.current_user:
groups = GroupList.get_user_groups(self.current_user.key, self.sql_session)
groups = []
_['current_user'] = self.current_user.to_dict() if self.current_user else None
_['current_groups'] = groups
return _
