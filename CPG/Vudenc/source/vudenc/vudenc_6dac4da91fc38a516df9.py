@handled_slot(bool)...
print(f"{'Locking' if checked else 'Unlocking'} thin etalon.")
self.lock_thin_etalon_action.setChecked(not checked)
self.matisse.set_thin_etalon_lock(checked)
self.lock_thin_etalon_action.setChecked(checked)
