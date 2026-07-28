@api.multi...
"""docstring"""
target_state_id = None
result = True
if 'state' in values:
target_state_id = values['state']
if target_state_id is not None:
transition = self._get_transition(target_state_id)
return super(ObjectWithStateMixin, self).write(values)
if transition:
result = True
if transition.write_before:
result = super(ObjectWithStateMixin, self).write(values)
self.exec_conditions(transition.preconditions, 'Pre')
self.exec_action(transition.action, transition.async_action)
self.exec_conditions(transition.postconditions, 'Post')
if transition.write_before:
return result
