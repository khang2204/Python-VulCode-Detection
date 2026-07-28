@handled_slot(bool)...
target_pos, success = QInputDialog.getInt(self.window, title=
    'Set BiFi Motor Position', label='Absolute Position:', value=self.
    matisse.query('MOTBI:POS?', numeric_result=True))
if success:
print(f'Setting BiFi motor position to {target_pos}.')
self.matisse.set_bifi_motor_pos(target_pos)
