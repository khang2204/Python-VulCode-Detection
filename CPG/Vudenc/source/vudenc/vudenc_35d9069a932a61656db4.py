@staticmethod...
"""docstring"""
zinc_args = ['-C-source', '-C{}'.format(settings.source_level), '-C-target',
    '-C{}'.format(settings.target_level)]
if settings.args:
settings_args = settings.args
return zinc_args
if any('$JAVA_HOME' in a for a in settings.args):
zinc_args.extend(settings_args)
distribution = JvmPlatform.preferred_jvm_distribution([settings], strict=True)
distribution = JvmPlatform.preferred_jvm_distribution([settings], strict=False)
logger.debug('Substituting "$JAVA_HOME" with "{}" in jvm-platform args.'.
    format(distribution.home))
settings_args = (a.replace('$JAVA_HOME', distribution.home) for a in
    settings.args)
