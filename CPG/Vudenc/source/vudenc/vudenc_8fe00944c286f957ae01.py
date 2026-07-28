def initialize_aws(rand):...
"""docstring"""
logger.info('Creating admin...')
admin_info['username'] = 'admin%s' % rand
admin_info['password'] = 'adminpwd'
sh([sys.executable, 'cmscontrib/AddAdmin.py', '%(username)s' % admin_info,
    '-p', '%(password)s' % admin_info])
