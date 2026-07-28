def get_temp_file_data(self):...
temp_file = open(TEMP_FILE, 'r')
temp_text = temp_file.read()
temp_file.close()
return temp_text
