def get_zip_url(self):...
uuid_path = f'{self.get_dg_folder()}/{str(self.fs_id)}.zip'
zip_file_path = f'{self.get_dg_folder()}/{self.get_name_as_slug()}.zip'
if os.path.isfile(uuid_path):
zip_url = uuid_path
if os.path.isfile(zip_file_path):
return zip_url
zip_url = zip_file_path
zip_url = 'no_path_found'
