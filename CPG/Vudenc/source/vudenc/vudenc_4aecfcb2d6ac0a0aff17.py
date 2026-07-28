def ensure_jupyterhub_service(prefix):...
"""docstring"""
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
