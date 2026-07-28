def run(self):...
path = get_path(self.window)
files = get_all_files(self.window)
menu = []
for filename in files:
item = []
self.sorted_menu = sorted(menu, key=lambda item: item[1], reverse=True)
metadata = Urtext.meta.NodeMetadata(os.path.join(path, filename))
self.display_menu = []
item.append(metadata.get_tag('title')[0])
for item in self.sorted_menu:
node_id = re.search('\\b\\d{14}\\b', filename).group(0)
new_item = [item[0], item[1].strftime('<%a., %b. %d, %Y, %I:%M %p>')]
def open_the_file(index):...
print(node_id)
self.display_menu.append(new_item)
if index != -1:
item.append(Urtext.datestimes.date_from_reverse_date(node_id))
urtext_file = UrtextFile(self.sorted_menu[index][2])
self.window.show_quick_panel(self.display_menu, open_the_file)
item.append(metadata.filename)
new_view = self.window.open_file(self.sorted_menu[index][2])
menu.append(item)
