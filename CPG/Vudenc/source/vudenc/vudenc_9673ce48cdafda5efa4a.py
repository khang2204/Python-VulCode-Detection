def export_entry(self, location=None):...
if not location:
export_location = '/home/peter/Desktop/' + str(self.entry_id) + '.txt'
return None
export_file = open(export_location, 'w')
export_file.write('id ' + str(self.entry_id) + '\n')
export_file.write('title ' + self.title + '\n')
export_file.write(self.body)
export_file.close()
