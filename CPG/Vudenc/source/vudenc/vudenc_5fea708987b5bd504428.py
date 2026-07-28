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
