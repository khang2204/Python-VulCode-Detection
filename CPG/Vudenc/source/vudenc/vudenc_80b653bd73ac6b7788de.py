def main(arguments=None):...
"""docstring"""
path = parse_arguments(arguments).message
for file in os.listdir(path):
if file.endswith('.txt'):
return
if db_get_file_details(file)['id'] > 0:
if db_get_file_details(file)['verified'] == 0:
db_insert_new_file(file)
if get_file_size(file) > db_get_file_details(file)['size']:
log_event(file)
db_update_file_details(file)
if get_time_now() - db_get_file_details(file)['age'] > 60:
log_event(file)
if db_get_file_details(file)['passes'] >= 3:
if hash_md5_for_file(file) == get_md5_from_file(file):
db_increment_passes(file)
db_verify_file_integrity(file)
