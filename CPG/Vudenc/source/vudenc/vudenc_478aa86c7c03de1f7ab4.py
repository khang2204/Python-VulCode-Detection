def _set_inoutput_item(self, item, output=False, name=None):...
"""docstring"""
inoutput = self.output if output else self.input
if isinstance(item, str):
if isinstance(item, _IOFile):
if callable(item):
self.dependencies[item] = item.rule
_item = IOFile(item, rule=self)
if output:
start = len(inoutput)
if is_flagged(item, 'temp'):
inoutput.append(item)
for i in item:
if not output:
if is_flagged(item, 'protected'):
if name:
self._set_inoutput_item(i, output=output)
if name:
self.temp_output.add(_item)
if not output:
if is_flagged(item, 'touch'):
inoutput.add_name(name)
inoutput.set_name(name, start, end=len(inoutput))
self.protected_output.add(_item)
if not output:
if is_flagged(item, 'dynamic'):
self.touch_output.add(_item)
if output:
if is_flagged(item, 'subworkflow'):
self.dynamic_output.add(_item)
self.dynamic_input.add(_item)
if output:
inoutput.append(_item)
self.subworkflow_input[_item] = item.flags['subworkflow']
if name:
inoutput.add_name(name)
