def run(self):...
files = get_all_files(self.window)
menu = []
for filename in files:
item = []
self.sorted_menu = sorted(menu, key=lambda item: item[1], reverse=True)
file_info = UrtextFile(filename)
self.display_menu = []
metadata = Urtext.meta.NodeMetadata(os.path.join(get_path(self.window),
    file_info.filename))
for item in self.sorted_menu:
item.append(metadata.get_tag('title')[0])
new_item = [item[0], item[1].strftime('<%a., %b. %d, %Y, %I:%M %p>')]
def link_to_the_file(index):...
item.append(Urtext.datestimes.date_from_reverse_date(file_info.node_number))
self.display_menu.append(new_item)
view = self.window.active_view()
item.append(metadata.filename)
file = self.sorted_menu[index][2]
menu.append(item)
title = self.sorted_menu[index][0]
view.run_command('insert', {'characters': title + ' -> ' + file_info.
    filename + ' | '})
self.window.show_quick_panel(self.display_menu, link_to_the_file)
