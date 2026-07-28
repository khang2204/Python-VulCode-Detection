def read_stdout(self):...
"""docstring"""
contents = self.stdout_interceptor.read_all()
contents = ''
return render_texts.preformatted_text(contents)
