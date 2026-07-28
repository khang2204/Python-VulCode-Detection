@classmethod...
super(DistributionLocator, cls).register_options(register)
human_readable_os_aliases = ', '.join('{}: [{}]'.format(str(key), ', '.join
    (sorted(val))) for key, val in OS_ALIASES.items())
register('--paths', advanced=True, type=dict, help=
    'Map of os names to lists of paths to jdks. These paths will be searched before everything else (before the JDK_HOME, JAVA_HOME, PATH environment variables) when locating a jvm to use. The same OS can be specified via several different aliases, according to this map: {}'
    .format(human_readable_os_aliases))
register('--minimum-version', advanced=True, help=
    'Minimum version of the JVM pants will use')
register('--maximum-version', advanced=True, help=
    'Maximum version of the JVM pants will use')
