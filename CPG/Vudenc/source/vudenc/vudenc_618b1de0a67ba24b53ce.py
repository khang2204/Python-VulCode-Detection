@handled_slot(bool)...
if checked:
for action in self.lock_actions:
for action in reversed(self.lock_actions):
if not action.isChecked():
if all([action.isChecked() for action in self.lock_actions]):
action.trigger()
action.trigger()
[action.setEnabled(False) for action in self.lock_actions]
self.lock_all_action.setChecked(False)
action.setEnabled(True)
print("Couldn't lock all laser components.")
