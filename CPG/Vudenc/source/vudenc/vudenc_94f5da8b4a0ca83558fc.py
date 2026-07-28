@handled_slot(bool)...
print(f"{'Locking' if checked else 'Unlocking'} piezo etalon.")
self.lock_piezo_etalon_action.setChecked(not checked)
self.matisse.set_piezo_etalon_lock(checked)
self.lock_piezo_etalon_action.setChecked(checked)
