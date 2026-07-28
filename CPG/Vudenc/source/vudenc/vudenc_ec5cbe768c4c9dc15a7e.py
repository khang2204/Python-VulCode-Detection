def return_to_left(self, view, return_view):...
if not view.is_loading():
view.window().focus_view(return_view)
sublime.set_timeout(lambda : self.return_to_left(view, return_view), 10)
view.window().focus_group(0)
