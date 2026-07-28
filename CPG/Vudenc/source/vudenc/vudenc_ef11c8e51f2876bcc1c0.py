"""Installation logic for TLJH"""
import argparse
import itertools
import logging
import os
import secrets
import subprocess
import sys
import time
from urllib.error import HTTPError
from urllib.request import urlopen, URLError
import pluggy
from tljh import apt, conda, hooks, migrator, systemd, traefik, user
from .config import CONFIG_DIR, CONFIG_FILE, HUB_ENV_PREFIX, INSTALL_PREFIX, STATE_DIR, USER_ENV_PREFIX
from .yaml import yaml
HERE = os.path.abspath(os.path.dirname(__file__))
logger = logging.getLogger('tljh')
def ensure_node():...
"""docstring"""
key = (
    b'\n-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\nComment: GPGTools - https://gpgtools.org\n\n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\n=CLGF\n-----END PGP PUBLIC KEY BLOCK-----\n    '
    .strip())
apt.trust_gpg_key(key)
apt.add_source('nodesource', 'https://deb.nodesource.com/node_10.x', 'main')
apt.install_packages(['nodejs'])
def remove_chp():...
"""docstring"""
if os.path.exists('/etc/systemd/system/configurable-http-proxy.service'):
if systemd.check_service_active('configurable-http-proxy.service'):
def ensure_jupyterhub_service(prefix):...
if systemd.check_service_enabled('configurable-http-proxy.service'):
systemd.stop_service('configurable-http-proxy.service')
logger.info('Cannot stop configurable-http-proxy...')
"""docstring"""
systemd.disable_service('configurable-http-proxy.service')
logger.info('Cannot disable configurable-http-proxy...')
systemd.uninstall_unit('configurable-http-proxy.service')
logger.info('Cannot uninstall configurable-http-proxy...')
os.makedirs(STATE_DIR, mode=448, exist_ok=True)
remove_chp()
systemd.reload_daemon()
hub_unit_template = f.read()
traefik_unit_template = f.read()
proxy_secret_path = os.path.join(STATE_DIR, 'traefik-api.secret')
if not os.path.exists(proxy_secret_path):
f.write(secrets.token_hex(32))
traefik.ensure_traefik_config(STATE_DIR)
unit_params = dict(python_interpreter_path=sys.executable,
    jupyterhub_config_path=os.path.join(HERE, 'jupyterhub_config.py'),
    install_prefix=INSTALL_PREFIX)
systemd.install_unit('jupyterhub.service', hub_unit_template.format(**
    unit_params))
systemd.install_unit('traefik.service', traefik_unit_template.format(**
    unit_params))
systemd.reload_daemon()
systemd.restart_service('jupyterhub')
systemd.restart_service('traefik')
systemd.enable_service('jupyterhub')
systemd.enable_service('traefik')
def ensure_jupyterlab_extensions():...
"""docstring"""
extensions = ['@jupyterlab/hub-extension',
    '@jupyter-widgets/jupyterlab-manager']
subprocess.check_output([os.path.join(USER_ENV_PREFIX, 'bin/jupyter'),
    'labextension', 'install'] + extensions)
def ensure_jupyterhub_package(prefix):...
"""docstring"""
conda.ensure_pip_packages(prefix, ['jupyterhub==0.9.4',
    'jupyterhub-dummyauthenticator==0.3.1',
    'jupyterhub-systemdspawner==0.11',
    'jupyterhub-firstuseauthenticator==0.12',
    'jupyterhub-nativeauthenticator==0.0.4',
    'jupyterhub-ldapauthenticator==1.2.2', 'oauthenticator==0.8.0'])
traefik.ensure_traefik_binary(prefix)
def ensure_usergroups():...
"""docstring"""
user.ensure_group('jupyterhub-admins')
user.ensure_group('jupyterhub-users')
logger.info('Granting passwordless sudo to JupyterHub admins...')
f.write('%jupyterhub-admins ALL = (ALL) NOPASSWD: ALL\n')
f.write('Defaults exempt_group = jupyterhub-admins\n')
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
def ensure_admins(admins):...
"""docstring"""
if not admins:
return
logger.info('Setting up admin users')
config_path = CONFIG_FILE
if os.path.exists(config_path):
config = yaml.load(f)
config = {}
config['users'] = config.get('users', {})
config['users']['admin'] = list(admins)
yaml.dump(config, f)
def ensure_jupyterhub_running(times=20):...
"""docstring"""
for i in range(times):
def ensure_symlinks(prefix):...
logger.info('Waiting for JupyterHub to come up ({}/{} tries)'.format(i + 1,
    times))
if h.code in [404, 502, 503]:
"""docstring"""
urlopen('http://127.0.0.1')
time.sleep(1)
if isinstance(e.reason, ConnectionRefusedError):
tljh_config_src = os.path.join(prefix, 'bin', 'tljh-config')
return
time.sleep(1)
tljh_config_dest = '/usr/bin/tljh-config'
if os.path.exists(tljh_config_dest):
if os.path.realpath(tljh_config_dest) != tljh_config_src:
os.symlink(tljh_config_src, tljh_config_dest)
return
def setup_plugins(plugins=None):...
"""docstring"""
if plugins:
conda.ensure_pip_packages(HUB_ENV_PREFIX, plugins)
pm = pluggy.PluginManager('tljh')
pm.add_hookspecs(hooks)
pm.load_setuptools_entrypoints('tljh')
return pm
