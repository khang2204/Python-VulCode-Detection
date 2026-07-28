def run_plugin_actions(plugin_manager, plugins):...
"""docstring"""
hook = plugin_manager.hook
apt_packages = list(set(itertools.chain(*hook.tljh_extra_apt_packages())))
if apt_packages:
logger.info('Installing {} apt packages collected from plugins: {}'.format(
    len(apt_packages), ' '.join(apt_packages)))
conda_packages = list(set(itertools.chain(*hook.
    tljh_extra_user_conda_packages())))
apt.install_packages(apt_packages)
if conda_packages:
logger.info('Installing {} conda packages collected from plugins: {}'.
    format(len(conda_packages), ' '.join(conda_packages)))
pip_packages = list(set(itertools.chain(*hook.tljh_extra_user_pip_packages())))
conda.ensure_conda_packages(USER_ENV_PREFIX, conda_packages)
if pip_packages:
logger.info('Installing {} pip packages collected from plugins: {}'.format(
    len(pip_packages), ' '.join(pip_packages)))
conda.ensure_pip_packages(USER_ENV_PREFIX, pip_packages)
