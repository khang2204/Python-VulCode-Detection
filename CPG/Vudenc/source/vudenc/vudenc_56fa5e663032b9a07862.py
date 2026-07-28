def decorate(ruleinfo):...
if ruleinfo.input:
rule.set_input(*ruleinfo.input[0], **ruleinfo.input[1])
if ruleinfo.output:
rule.set_output(*ruleinfo.output[0], **ruleinfo.output[1])
if ruleinfo.params:
rule.set_params(*ruleinfo.params[0], **ruleinfo.params[1])
if ruleinfo.threads:
if not isinstance(ruleinfo.threads, int):
if ruleinfo.resources:
rule.resources['_cores'] = ruleinfo.threads
args, resources = ruleinfo.resources
if ruleinfo.priority:
if args:
if not isinstance(ruleinfo.priority, int) and not isinstance(ruleinfo.
if ruleinfo.version:
if not all(map(lambda r: isinstance(r, int), resources.values())):
rule.priority = ruleinfo.priority
rule.version = ruleinfo.version
if ruleinfo.log:
rule.resources.update(resources)
rule.set_log(*ruleinfo.log[0], **ruleinfo.log[1])
if ruleinfo.message:
rule.message = ruleinfo.message
if ruleinfo.benchmark:
rule.benchmark = ruleinfo.benchmark
rule.norun = ruleinfo.norun
rule.docstring = ruleinfo.docstring
rule.run_func = ruleinfo.func
rule.shellcmd = ruleinfo.shellcmd
ruleinfo.func.__name__ = '__{}'.format(name)
self.globals[ruleinfo.func.__name__] = ruleinfo.func
setattr(rules, name, rule)
return ruleinfo.func
