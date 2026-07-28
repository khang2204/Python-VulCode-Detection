@handled_slot(bool)...
print(f"{'Locking' if checked else 'Unlocking'} fast piezo.")
self.lock_fast_piezo_action.setChecked(not checked)
self.matisse.set_piezo_etalon_lock(checked)
self.lock_fast_piezo_action.setChecked(checked)
