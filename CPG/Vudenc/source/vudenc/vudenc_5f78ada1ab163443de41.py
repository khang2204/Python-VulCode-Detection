def setup_menus(self):...
menu_bar = self.window.menuBar()
console_menu = menu_bar.addMenu('Console')
self.clear_log_area_action = console_menu.addAction('Clear Log')
self.open_idle_action = console_menu.addAction('Open Python Shell...')
self.restart_action = console_menu.addAction('Restart')
set_menu = menu_bar.addMenu('Set')
self.set_wavelength_action = set_menu.addAction('Wavelength')
self.set_bifi_approx_wavelength_action = set_menu.addAction(
    'BiFi Approx. Wavelength')
self.set_bifi_motor_pos_action = set_menu.addAction('BiFi Motor Position')
self.set_thin_eta_motor_pos_action = set_menu.addAction(
    'Thin Etalon Motor Position')
scan_menu = menu_bar.addMenu('Scan')
self.bifi_scan_action = scan_menu.addAction('Birefringent Filter')
self.thin_eta_scan_action = scan_menu.addAction('Thin Etalon')
lock_menu = menu_bar.addMenu('Lock')
self.lock_all_action = lock_menu.addAction('Lock All')
self.lock_all_action.setCheckable(True)
self.lock_slow_piezo_action = lock_menu.addAction('Lock Slow Piezo')
self.lock_slow_piezo_action.setCheckable(True)
self.lock_thin_etalon_action = lock_menu.addAction('Lock Thin Etalon')
self.lock_thin_etalon_action.setCheckable(True)
self.lock_piezo_etalon_action = lock_menu.addAction('Lock Piezo Etalon')
self.lock_piezo_etalon_action.setCheckable(True)
self.lock_fast_piezo_action = lock_menu.addAction('Lock Fast Piezo')
self.lock_fast_piezo_action.setCheckable(True)
tools_menu = menu_bar.addMenu('Tools')
self.lock_actions = [self.lock_slow_piezo_action, self.
    lock_thin_etalon_action, self.lock_piezo_etalon_action, self.
    lock_fast_piezo_action]
