def get_dg_folder(self):...
uuid_dir = f'{settings.MEDIA_ROOT}{str(self.fs_id)}'
name_dir = f'{settings.MEDIA_ROOT}{self.get_name_as_slug()}'
if bool(self.csv.name):
p = PurePath(self.csv.path)
if os.path.isdir(uuid_dir):
csv_folder = p.parts[-2]
return uuid_dir
if bool(self.csv.name) and os.path.isdir(csv_fullfolderpath):
csv_fullfolderpath = f'{settings.MEDIA_ROOT}{csv_folder}'
return csv_fullfolderpath
return 'no_folder_found'
