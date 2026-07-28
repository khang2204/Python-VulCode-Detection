def log_event(path):...
"""docstring"""
time_now = get_time_now()
file_size = db_get_file_details(path)['size']
file_age = db_get_file_details(path)['age']
file_passes = db_get_file_details(path)['passes']
print(time_now, '>', path, ' Current size: ', file_size, ' Last updated: ',
    file_age, ' Number of passes: ', file_passes)
return
