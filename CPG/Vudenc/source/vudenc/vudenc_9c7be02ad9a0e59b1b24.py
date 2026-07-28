@handled_slot(bool)...
target_pos, success = QInputDialog.getInt(self.window, title=
    'Set Thin Etalon Motor Position', label='Absolute Position:', value=
    self.matisse.query('MOTTE:POS?', numeric_result=True))
if success:
print(f'Setting thin etalon motor position to {target_pos}.')
self.matisse.set_thin_etalon_motor_pos(target_pos)
