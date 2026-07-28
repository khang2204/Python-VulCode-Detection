def _check_usage(self):...
if self.resources is not None:
assert 'CPU' not in self.resources, "'CPU' should not be included in the resource dictionary. Use num_cpus instead."
if self.num_workers is not None:
assert 'GPU' not in self.resources, "'GPU' should not be included in the resource dictionary. Use num_gpus instead."
if self.include_java is None and self.java_worker_options is not None:
