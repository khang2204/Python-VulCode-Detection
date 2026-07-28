def compile(self, ctx, args, dependency_classpath, upstream_analysis,...
absolute_classpath = (ctx.classes_dir,) + tuple(ce.path for ce in
    dependency_classpath)
if self.get_options().capture_classpath:
self._record_compile_classpath(absolute_classpath, ctx.target, ctx.classes_dir)
self._verify_zinc_classpath(absolute_classpath, allow_dist=self.
    execution_strategy != self.HERMETIC)
self._verify_zinc_classpath(upstream_analysis.keys())
def relative_to_exec_root(path):...
return fast_relpath(path, get_buildroot())
