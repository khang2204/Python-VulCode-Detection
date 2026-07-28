def setup_action_listeners(self):...
self.clear_log_area_action.triggered.connect(self.clear_log_area)
self.open_idle_action.triggered.connect(self.open_idle)
self.restart_action.triggered.connect(self.restart)
self.set_wavelength_action.triggered.connect(self.set_wavelength_dialog)
self.set_bifi_approx_wavelength_action.triggered.connect(self.
    set_bifi_approx_wavelength_dialog)
self.set_bifi_motor_pos_action.triggered.connect(self.set_bifi_motor_pos_dialog
    )
self.set_thin_eta_motor_pos_action.triggered.connect(self.
    set_thin_eta_motor_pos_dialog)
self.bifi_scan_action.triggered.connect(self.start_bifi_scan)
self.thin_eta_scan_action.triggered.connect(self.start_thin_etalon_scan)
self.lock_all_action.triggered.connect(self.toggle_lock_all)
self.lock_slow_piezo_action.triggered.connect(self.toggle_slow_piezo_lock)
self.lock_thin_etalon_action.triggered.connect(self.toggle_thin_etalon_lock)
self.lock_piezo_etalon_action.triggered.connect(self.toggle_piezo_etalon_lock)
self.lock_fast_piezo_action.triggered.connect(self.toggle_fast_piezo_lock)
