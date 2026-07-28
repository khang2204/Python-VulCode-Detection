def get_file_links_in_file(self, filename):...
contents = this_file.read()
links = re.findall('->\\s+(?!http)([\\w\\.\\/]+)', contents)
return links
