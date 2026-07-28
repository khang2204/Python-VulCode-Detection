@handled_slot(bool)...
print(f"{'Locking' if checked else 'Unlocking'} slow piezo.")
self.lock_slow_piezo_action.setChecked(not checked)
self.matisse.set_slow_piezo_lock(checked)
self.lock_slow_piezo_action.setChecked(checked)
