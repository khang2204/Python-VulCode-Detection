def write_body_to_temp_file(self):...
temp_file = open(TEMP_FILE, 'w')
temp_file.write(self.body)
temp_file.close()
return None
