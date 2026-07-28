def main():...
from .log import init_logging
init_logging()
argparser = argparse.ArgumentParser()
argparser.add_argument('--admin', nargs='*', help=
    'List of usernames set to be admin')
argparser.add_argument('--user-requirements-txt-url', help=
    'URL to a requirements.txt file that should be installed in the user enviornment'
    )
argparser.add_argument('--plugin', nargs='*', help=
    'Plugin pip-specs to install')
args = argparser.parse_args()
pm = setup_plugins(args.plugin)
ensure_config_yaml(pm)
ensure_admins(args.admin)
ensure_usergroups()
ensure_user_environment(args.user_requirements_txt_url)
logger.info('Setting up JupyterHub...')
ensure_node()
ensure_jupyterhub_package(HUB_ENV_PREFIX)
ensure_jupyterlab_extensions()
ensure_jupyterhub_service(HUB_ENV_PREFIX)
ensure_jupyterhub_running()
ensure_symlinks(HUB_ENV_PREFIX)
run_plugin_actions(pm, args.plugin)
logger.info('Done!')
