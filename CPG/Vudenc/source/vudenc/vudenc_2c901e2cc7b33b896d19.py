def ensure_user_environment(user_requirements_txt_file):...
"""docstring"""
logger.info('Setting up user environment...')
miniconda_version = '4.5.4'
miniconda_installer_md5 = 'a946ea1d0c4a642ddf0c3a26a18bb16d'
if not conda.check_miniconda_version(USER_ENV_PREFIX, miniconda_version):
logger.info('Downloading & setting up user environment...')
apt.install_packages(['gcc'])
conda.install_miniconda(installer_path, USER_ENV_PREFIX)
conda.ensure_conda_packages(USER_ENV_PREFIX, ['conda==4.5.8'])
conda.ensure_pip_packages(USER_ENV_PREFIX, ['jupyterhub==0.9.4',
    'notebook==5.7.0', 'jupyterlab==0.35.3', 'nteract-on-jupyter==1.9.12',
    'nbgitpuller==0.6.1', 'nbresuse==0.3.0', 'ipywidgets==7.4.2',
    'tornado<6.0'])
if user_requirements_txt_file:
conda.ensure_pip_requirements(USER_ENV_PREFIX, user_requirements_txt_file)
