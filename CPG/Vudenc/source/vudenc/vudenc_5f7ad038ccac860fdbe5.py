@handled_slot(bool)...
target_wavelength, success = QInputDialog.getDouble(self.window, title=
    'Set Approx. Wavelength', label='Wavelength (nm): ', value=self.matisse
    .query('MOTBI:WL?', numeric_result=True))
if success:
print(f'Setting BiFi approximate wavelength to {target_wavelength} nm...')
self.matisse.set_bifi_wavelength(target_wavelength)
