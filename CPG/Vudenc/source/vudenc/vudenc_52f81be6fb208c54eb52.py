def format_wildcards(self, string, **variables):...
"""docstring"""
_variables = dict()
_variables.update(self.rule.workflow.globals)
_variables.update(dict(input=self.input, output=self.output, params=self.
    params, wildcards=self._format_wildcards, threads=self.threads,
    resources=self.resources, log=self.log, version=self.rule.version, rule
    =self.rule.name))
_variables.update(variables)
return format(string, **_variables)
