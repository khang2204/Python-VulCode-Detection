def get_links_to_file(self, filename):...
visited_files = []
if filename == '':
return []
files = Urtext.get_all_files(self.view.window())
links_to_file = []
for file in files:
if file[-4:] == '.txt':
return links_to_file
contents = this_file.read()
links = re.findall('-> ' + filename.replace('.txt', ''), contents)
for link in links:
links_to_file.append(file)
