def val(fn):...
def newfn(self, *a, **env):...
for validator in simple_vals:
if request.method == 'POST' and hasattr(self, 'ajax_login_redirect'):
return newfn
validator(env)
kw = self.build_arg_list(fn, env)
return self.ajax_login_redirect('/')
return self.intermediate_redirect('/login')
for var, validator in param_vals.iteritems():
kw[var] = validator(env)
return fn(self, *a, **kw)
