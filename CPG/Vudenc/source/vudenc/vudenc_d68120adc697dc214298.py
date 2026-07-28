def run(self, edit):...
filename = self.view.window().extract_variables()['file_name']
self.view.show_popup('`' + filename + '` copied to the clipboard')
sublime.set_clipboard(filename)
