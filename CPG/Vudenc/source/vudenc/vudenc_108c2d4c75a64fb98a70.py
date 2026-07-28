def fetch_data_via_ftp(ftp_config, local_directory):...
"""docstring"""
if ftp_config.enabled:
create_directory_tree(local_directory)
if ftp_config.use_tls:
ftp = FTP_TLS(ftp_config.server)
ftp = FTP(ftp_config.server)
ftp.login(ftp_config.username, ftp_config.password)
ftp.login(ftp_config.username, ftp_config.password)
ftp.prot_p()
if not ftp_config.files:
fetch_data_via_ftp_recursive(ftp=ftp, local_directory=local_directory,
    remote_directory=ftp_config.directory)
ftp.cwd(ftp_config.directory)
ftp.close()
file_counter = 1
file_list_total = len(ftp_config.files)
for remote_filename in ftp_config.files:
local_filename = remote_filename
filepath = os.path.join(local_directory, local_filename)
if not os.path.exists(filepath):
print('[Setup][FTP] ({}/{}) File already exists. Skipping: {}'.format(
    file_counter, file_list_total, filepath))
ftp.retrbinary('RETR %s' % remote_filename, local_file.write)
print('[Setup][FTP] ({}/{}) Error downloading file. Skipping: {}'.format(
    file_counter, file_list_total, filepath))
file_counter = file_counter + 1
print('[Setup][FTP] ({}/{}) File downloaded: {}'.format(file_counter,
    file_list_total, filepath))
local_file.close()
os.remove(filepath)
