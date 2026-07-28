return wrapper

@staticmethod
@silence_streams
def make_backup(orig_file, data_path, full_file_name):
    if os.path.isfile(full_file_name):
        epoch_time = int(time.time())
        bak_file_path = "%s/bak%d_%s" % (data_path, epoch_time,
                                         orig_file.name)
        # intended vulnerability for command injection
        os.system("cp %s %s" % (full_file_name, bak_file_path))
        return bak_file_path
