import os
import queue
import subprocess
import sys
import traceback
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QWidget, QTextEdit, QInputDialog, QMessageBox, QApplication
from matisse import Matisse
from .handled_decorators import handled_function, handled_slot
from .logging_stream import LoggingStream
from .status_monitor import StatusMonitor
from .threading import ExitFlag, LoggingThread
EXIT_CODE_RESTART = 42
def __init__(self, *args, **kwargs):...
super().__init__(*args, **kwargs)
self.setup_logging()
self.setup_window()
self.setup_menus()
self.setup_action_listeners()
self.setup_log_window()
self.setup_matisse()
self.setup_widgets()
self.aboutToQuit.connect(self.clean_up)
container = QWidget()
container.setLayout(self.layout)
self.window.setCentralWidget(container)
self.window.show()
def setup_logging(self):...
self.log_area = QTextEdit()
self.log_area.setReadOnly(True)
self.log_queue = queue.Queue()
self.log_stream = LoggingStream(self.log_queue)
self.log_thread = LoggingThread(self.log_queue, parent=self)
self.log_thread.message_received.connect(self.log)
self.log_thread.start()
def setup_window(self):...
self.window = window = QMainWindow()
self.layout = QVBoxLayout()
window.setWindowTitle('Matisse Controller')
window.resize(600, 200)
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
def setup_log_window(self):...
self.layout.addWidget(self.log_area)
@handled_function...
self.status_monitor_queue = queue.Queue(maxsize=1)
self.status_monitor = StatusMonitor(self.matisse, self.status_monitor_queue)
self.layout.addWidget(self.status_monitor)
@handled_function...
self.matisse: Matisse = Matisse(device_id=sys.argv[1], wavemeter_port=sys.
    argv[2])
self.matisse: Matisse = None
@pyqtSlot()...
self.status_monitor_queue.put(ExitFlag())
self.status_monitor.update_thread.wait()
self.log_queue.put(ExitFlag())
self.log_thread.wait()
@pyqtSlot(str)...
self.log_area.moveCursor(QTextCursor.End)
self.log_area.insertPlainText(message)
def error_dialog(self):...
stack = list(traceback.format_exception(*sys.exc_info()))
desired_width = min(max([len(line) for line in stack]), 185)
description = stack.pop()
print(description, end='')
stack = filter(lambda item: os.path.join('gui', 'handled_decorators.py') not in
    item, stack)
dialog = QMessageBox(icon=QMessageBox.Critical)
dialog.setWindowTitle('Error')
dialog.setText(f"""{description + '_' * desired_width}

{''.join(stack)}""")
dialog.exec()
@handled_slot(bool)...
self.log_area.clear()
@handled_slot(bool)...
print('Opening IDLE.')
subprocess.Popen(
    'python -m idlelib -t "Matisse Controller - Python Shell" -c "from matisse import Matisse; '
     +
    'matisse = Matisse(); print(\'Access the Matisse using \\\'matisse.[method]\\\'\')"'
    )
@handled_slot(bool)...
self.exit(self.EXIT_CODE_RESTART)
@handled_slot(bool)...
target_wavelength, success = QInputDialog.getDouble(self.window, title=
    'Set Wavelength', label='Wavelength (nm): ', value=self.matisse.
    target_wavelength)
if success:
print(f'Setting wavelength to {target_wavelength} nm...')
@handled_slot(bool)...
self.matisse.set_wavelength(target_wavelength)
target_wavelength, success = QInputDialog.getDouble(self.window, title=
    'Set Approx. Wavelength', label='Wavelength (nm): ', value=self.matisse
    .query('MOTBI:WL?', numeric_result=True))
if success:
print(f'Setting BiFi approximate wavelength to {target_wavelength} nm...')
@handled_slot(bool)...
self.matisse.set_bifi_wavelength(target_wavelength)
target_pos, success = QInputDialog.getInt(self.window, title=
    'Set BiFi Motor Position', label='Absolute Position:', value=self.
    matisse.query('MOTBI:POS?', numeric_result=True))
if success:
print(f'Setting BiFi motor position to {target_pos}.')
@handled_slot(bool)...
self.matisse.set_bifi_motor_pos(target_pos)
target_pos, success = QInputDialog.getInt(self.window, title=
    'Set Thin Etalon Motor Position', label='Absolute Position:', value=
    self.matisse.query('MOTTE:POS?', numeric_result=True))
if success:
print(f'Setting thin etalon motor position to {target_pos}.')
@handled_slot(bool)...
self.matisse.set_thin_etalon_motor_pos(target_pos)
print('Starting BiFi scan...')
self.matisse.birefringent_filter_scan()
@handled_slot(bool)...
print('Starting thin etalon scan...')
self.matisse.thin_etalon_scan()
@handled_slot(bool)...
if checked:
for action in self.lock_actions:
for action in reversed(self.lock_actions):
if not action.isChecked():
if all([action.isChecked() for action in self.lock_actions]):
action.trigger()
@handled_slot(bool)...
action.trigger()
[action.setEnabled(False) for action in self.lock_actions]
self.lock_all_action.setChecked(False)
action.setEnabled(True)
print(f"{'Locking' if checked else 'Unlocking'} slow piezo.")
print("Couldn't lock all laser components.")
self.lock_slow_piezo_action.setChecked(not checked)
self.matisse.set_slow_piezo_lock(checked)
self.lock_slow_piezo_action.setChecked(checked)
@handled_slot(bool)...
print(f"{'Locking' if checked else 'Unlocking'} thin etalon.")
self.lock_thin_etalon_action.setChecked(not checked)
self.matisse.set_thin_etalon_lock(checked)
self.lock_thin_etalon_action.setChecked(checked)
@handled_slot(bool)...
print(f"{'Locking' if checked else 'Unlocking'} piezo etalon.")
self.lock_piezo_etalon_action.setChecked(not checked)
self.matisse.set_piezo_etalon_lock(checked)
self.lock_piezo_etalon_action.setChecked(checked)
@handled_slot(bool)...
print(f"{'Locking' if checked else 'Unlocking'} fast piezo.")
self.lock_fast_piezo_action.setChecked(not checked)
self.matisse.set_piezo_etalon_lock(checked)
self.lock_fast_piezo_action.setChecked(checked)
