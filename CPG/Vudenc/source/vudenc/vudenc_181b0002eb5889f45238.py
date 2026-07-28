def __init__(self, rule, dag, targetfile=None, format_wildcards=None):...
self.rule = rule
self.dag = dag
self.targetfile = targetfile
self.wildcards_dict = self.rule.get_wildcards(targetfile)
self.wildcards = Wildcards(fromdict=self.wildcards_dict)
self._format_wildcards = (self.wildcards if format_wildcards is None else
    Wildcards(fromdict=format_wildcards))
(self.input, self.output, self.params, self.log, self.benchmark, self.
    ruleio, self.dependencies) = rule.expand_wildcards(self.wildcards_dict)
self.resources_dict = {name: min(self.rule.workflow.global_resources.get(
    name, res), res) for name, res in rule.resources.items()}
self.threads = self.resources_dict['_cores']
self.resources = Resources(fromdict=self.resources_dict)
self._inputsize = None
self.dynamic_output, self.dynamic_input = set(), set()
self.temp_output, self.protected_output = set(), set()
self.touch_output = set()
self.subworkflow_input = dict()
for f in self.output:
f_ = self.ruleio[f]
for f in self.input:
if f_ in self.rule.dynamic_output:
f_ = self.ruleio[f]
self._hash = self.rule.__hash__()
self.dynamic_output.add(f)
if f_ in self.rule.temp_output:
if f_ in self.rule.dynamic_input:
if True or not self.dynamic_output:
self.temp_output.add(f)
if f_ in self.rule.protected_output:
self.dynamic_input.add(f)
if f_ in self.rule.subworkflow_input:
for o in self.output:
self.protected_output.add(f)
if f_ in self.rule.touch_output:
self.subworkflow_input[f] = self.rule.subworkflow_input[f_]
self._hash ^= o.__hash__()
self.touch_output.add(f)
