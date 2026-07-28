def missing_output(self, requested=None):...
"""docstring"""
files = set()
if self.benchmark and (requested is None or self.benchmark in requested):
if not self.benchmark.exists:
for f, f_ in zip(self.output, self.rule.output):
files.add(self.benchmark)
if requested is None or f in requested:
return files
if f in self.dynamic_output:
if not self.expand_dynamic(f_, restriction=self.wildcards, omit_value=
if not f.exists:
files.add('{} (dynamic)'.format(f_))
files.add(f)
