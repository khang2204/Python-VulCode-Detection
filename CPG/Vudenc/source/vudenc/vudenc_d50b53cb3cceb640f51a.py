def start_gui(control_center):...
app = QtGui.QApplication(sys.argv)
main_window = QtGui.QMainWindow()
ui = hyperGUI.UiMainWindow()
ui.ui_init(main_window, control_center)
main_window.show()
sys.exit(app.exec_())
