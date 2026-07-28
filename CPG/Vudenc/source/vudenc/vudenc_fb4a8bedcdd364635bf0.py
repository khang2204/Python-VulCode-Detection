def fetch_data_via_ftp_recursive(ftp, local_directory, remote_directory,...
"""docstring"""
if remote_subdirs_list is not None and len(remote_subdirs_list) > 0:
remote_path_relative = '/'.join(remote_subdirs_list)
remote_subdirs_list = []
remote_path_absolute = ('/' + remote_directory + '/' + remote_path_relative +
    '/')
remote_path_relative = ''
local_path = local_directory + '/' + remote_path_relative
print('[Setup][FTP] Error: Could not change to: {}'.format(
    remote_path_absolute))
ftp.cwd(remote_path_absolute)
remote_path_absolute = '/' + remote_directory + '/'
os.mkdir(local_path)
file_list = ftp.nlst()
print('[Setup][FTP] Created local folder: {}'.format(local_path))
file_counter = 1
file_list_total = len(file_list)
for file in file_list:
file_path_local = local_directory + '/' + remote_path_relative + '/' + file
if not os.path.isfile(file_path_local):
print('[Setup][FTP] ({}/{}) File already exists. Skipping: {}'.format(
    file_counter, file_list_total, file_path_local))
ftp.cwd(remote_path_absolute + file)
temp = ftp.nlst()
file_counter = file_counter + 1
print('[Setup][FTP] Switching to directory: {}'.format(remote_path_relative +
    '/' + file))
if not os.path.isfile(file_path_local):
new_remote_subdirs_list = remote_subdirs_list.copy()
ftp.retrbinary('RETR {}'.format(file), local_file.write)
new_remote_subdirs_list.append(file)
print('[Setup][FTP] ({}/{}) File downloaded: {}'.format(file_counter,
    file_list_total, file_path_local))
fetch_data_via_ftp_recursive(ftp=ftp, local_directory=local_directory,
    remote_directory=remote_directory, remote_subdirs_list=
    new_remote_subdirs_list)
ftp.cwd(remote_path_absolute)
