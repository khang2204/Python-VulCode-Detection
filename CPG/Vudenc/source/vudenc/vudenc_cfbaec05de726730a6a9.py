@handled_slot(bool)...
target_wavelength, success = QInputDialog.getDouble(self.window, title=
    'Set Wavelength', label='Wavelength (nm): ', value=self.matisse.
    target_wavelength)
if success:
print(f'Setting wavelength to {target_wavelength} nm...')
self.matisse.set_wavelength(target_wavelength)
