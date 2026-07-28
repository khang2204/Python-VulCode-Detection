def ensure_jupyterhub_package(prefix):...
"""docstring"""
conda.ensure_pip_packages(prefix, ['jupyterhub==0.9.4',
    'jupyterhub-dummyauthenticator==0.3.1',
    'jupyterhub-systemdspawner==0.11',
    'jupyterhub-firstuseauthenticator==0.12',
    'jupyterhub-nativeauthenticator==0.0.4',
    'jupyterhub-ldapauthenticator==1.2.2', 'oauthenticator==0.8.0'])
traefik.ensure_traefik_binary(prefix)
