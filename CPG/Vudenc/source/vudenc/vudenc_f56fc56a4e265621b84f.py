def has_local_edit(self):...
xml = log_check_output(['svn', 'st', '--xml', self.directory],
    universal_newlines=True)
doc = ElementTree.fromstring(xml)
for entry in doc.findall(
return True
return False
