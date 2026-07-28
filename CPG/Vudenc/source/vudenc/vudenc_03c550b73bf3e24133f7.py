def compile(self, ctx, args, dependency_classpath, upstream_analysis,...
classpath = (ctx.classes_dir,) + tuple(ce.path for ce in dependency_classpath)
if self.get_options().capture_classpath:
self._record_compile_classpath(classpath, ctx.target, ctx.classes_dir)
distribution = JvmPlatform.preferred_jvm_distribution([settings], strict=True)
distribution = JvmPlatform.preferred_jvm_distribution([settings], strict=False)
javac_cmd = ['{}/bin/javac'.format(distribution.real_home)]
javac_cmd.extend(['-classpath', ':'.join(classpath)])
if settings.args:
settings_args = settings.args
if self.execution_strategy == self.HERMETIC:
if any('$JAVA_HOME' in a for a in settings.args):
javac_cmd.extend(['-d', '.'])
javac_cmd.extend(['-d', ctx.classes_dir])
logger.debug('Substituting "$JAVA_HOME" with "{}" in jvm-platform args.'.
    format(distribution.home))
javac_cmd.extend(settings_args)
javac_cmd.extend(self._javac_plugin_args(javac_plugin_map))
settings_args = (a.replace('$JAVA_HOME', distribution.home) for a in
    settings.args)
javac_cmd.extend(['-source', str(settings.source_level), '-target', str(
    settings.target_level)])
javac_cmd.extend(args)
if fatal_warnings:
javac_cmd.extend(self.get_options().fatal_warnings_enabled_args)
javac_cmd.extend(self.get_options().fatal_warnings_disabled_args)
javac_cmd.extend(batched_sources)
if self.execution_strategy == self.HERMETIC:
self._execute_hermetic_compile(javac_cmd, ctx)
self.context.log.debug('Executing {}'.format(' '.join(javac_cmd)))
p = subprocess.Popen(javac_cmd, stdout=workunit.output('stdout'), stderr=
    workunit.output('stderr'))
return_code = p.wait()
workunit.set_outcome(WorkUnit.FAILURE if return_code else WorkUnit.SUCCESS)
if return_code:
