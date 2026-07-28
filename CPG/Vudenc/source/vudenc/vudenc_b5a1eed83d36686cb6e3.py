@classmethod...
super(NodeDistribution.Factory, cls).register_options(register)
register('--supportdir', advanced=True, default='bin/node', help=
    'Find the Node distributions under this dir.  Used as part of the path to lookup the distribution with --binary-util-baseurls and --pants-bootstrapdir'
    )
register('--version', advanced=True, default='6.9.1', help=
    'Node distribution version.  Used as part of the path to lookup the distribution with --binary-util-baseurls and --pants-bootstrapdir'
    )
register('--package-manager', advanced=True, default='npm', fingerprint=
    True, choices=NodeDistribution.VALID_PACKAGE_MANAGER_LIST.keys(), help=
    'Default package manager config for repo. Should be one of {}'.format(
    NodeDistribution.VALID_PACKAGE_MANAGER_LIST.keys()))
register('--yarnpkg-version', advanced=True, default='v0.19.1', fingerprint
    =True, help='Yarnpkg version. Used for binary utils')
