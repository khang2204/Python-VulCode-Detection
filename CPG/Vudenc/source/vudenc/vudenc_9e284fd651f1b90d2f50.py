def __init__(self, *args, **kwargs):...
super(BaseZincCompile, self).__init__(*args, **kwargs)
self._processor_info_dir = os.path.join(self.workdir, 'apt-processor-info')
ZincCompile.validate_arguments(self.context.log, self.get_options().
    whitelisted_args, self._args)
if self.execution_strategy == self.HERMETIC:
fast_relpath(self.get_options().pants_workdir, get_buildroot())
if self.get_options().use_classpath_jars:
