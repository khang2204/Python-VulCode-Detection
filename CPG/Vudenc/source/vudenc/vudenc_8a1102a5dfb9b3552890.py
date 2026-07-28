def aws(cred, env, private_data_dir):...
env['AWS_ACCESS_KEY_ID'] = cred.get_input('username', default='')
env['AWS_SECRET_ACCESS_KEY'] = cred.get_input('password', default='')
if cred.has_input('security_token'):
env['AWS_SECURITY_TOKEN'] = cred.get_input('security_token', default='')
