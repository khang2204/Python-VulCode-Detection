def add_common_arguments(parser):...
group = parser.add_argument_group('Common parameters')
group.add_argument('--debug', action='store_true', default=False, help=
    'Show debug messages')
group.add_argument('--repos', action='store_true', default=False, help=
    'List repositories which the command operates on')
group.add_argument('path', nargs='?', default=os.curdir, help=
    'Base path to look for repositories')
