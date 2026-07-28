def ensure_jupyterlab_extensions():...
"""docstring"""
extensions = ['@jupyterlab/hub-extension',
    '@jupyter-widgets/jupyterlab-manager']
subprocess.check_output([os.path.join(USER_ENV_PREFIX, 'bin/jupyter'),
    'labextension', 'install'] + extensions)
