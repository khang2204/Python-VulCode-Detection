def remote_exists(self, host, path):...
p = psutil.Popen(['ssh', host, 'ls', '-Fa', path.as_posix()], stdout=PIPE,
    stderr=PIPE)
main_output, main_error = p.communicate()
error = main_error.decode(encoding='UTF-8')
error_matched = re.search('No such file or directory', error)
if error_matched is not None:
logging.debug('Path not found')
return True
return False
