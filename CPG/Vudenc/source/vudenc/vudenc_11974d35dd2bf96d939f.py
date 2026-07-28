def remote_iterdir(self, host, path):...
p = psutil.Popen(['ssh', host, 'ls', '-Fa', path.as_posix()], stdout=PIPE,
    stderr=PIPE)
main_output, main_error = p.communicate()
logging.debug(main_error.decode(encoding='UTF-8'))
return main_output.decode(encoding='UTF-8').split('\n')
