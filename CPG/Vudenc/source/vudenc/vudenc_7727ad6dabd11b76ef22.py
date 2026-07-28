@staticmethod...
return ' '.join(escape_path_argument(s) for s in (sys.executable, os.path.
    join(os.path.dirname(os.path.realpath(__file__)),
    'run_shell_command_testfiles', scriptname)))
