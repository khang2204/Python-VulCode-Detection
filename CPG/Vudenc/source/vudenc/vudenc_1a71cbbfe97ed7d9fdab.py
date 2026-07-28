def prepare(self):...
"""docstring"""
self.check_protected_output()
unexpected_output = self.dag.reason(self).missing_output.intersection(self.
    existing_output)
if unexpected_output:
logger.warning(
    """Warning: the following output files of rule {} were not present when the DAG was created:
{}"""
    .format(self.rule, unexpected_output))
if self.dynamic_output:
for f, _ in chain(*map(partial(self.expand_dynamic, restriction=self.
for f, f_ in zip(self.output, self.rule.output):
os.remove(f)
f.prepare()
for f in self.log:
f.prepare()
if self.benchmark:
self.benchmark.prepare()
