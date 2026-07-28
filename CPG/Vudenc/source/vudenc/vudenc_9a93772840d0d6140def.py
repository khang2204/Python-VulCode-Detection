def link_to_the_file(index):...
view = self.window.active_view()
file = self.sorted_menu[index][2]
title = self.sorted_menu[index][0]
view.run_command('insert', {'characters': title + ' -> ' + file_info.
    filename + ' | '})
