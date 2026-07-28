@classmethod...
super(BuildSetupRequiresPex, cls).register_options(register)
register('--setuptools-version', advanced=True, fingerprint=True, default=
    '40.6.3', help=
    'The setuptools version to use when executing `setup.py` scripts.')
register('--wheel-version', advanced=True, fingerprint=True, default=
    '0.32.3', help=
    'The wheel version to use when executing `setup.py` scripts.')
