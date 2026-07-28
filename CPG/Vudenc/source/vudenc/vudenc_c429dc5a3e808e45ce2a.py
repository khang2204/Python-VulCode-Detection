def ensure_usergroups():...
"""docstring"""
user.ensure_group('jupyterhub-admins')
user.ensure_group('jupyterhub-users')
logger.info('Granting passwordless sudo to JupyterHub admins...')
f.write('%jupyterhub-admins ALL = (ALL) NOPASSWD: ALL\n')
f.write('Defaults exempt_group = jupyterhub-admins\n')
