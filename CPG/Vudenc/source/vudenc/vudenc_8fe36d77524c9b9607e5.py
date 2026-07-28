def exec_action(self, action, async_action):...
if action:
context = {'active_model': self._name, 'active_id': self.id, 'active_ids':
    self.ids}
if async_action:
action.with_delay().run_async(context)
action.with_context(context).run()
