def main():...
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
parser = argparse.ArgumentParser()
parser.add_argument('--config', '-c', type=str, default='test.yaml', help=
    'YAML config file. see sample-config.yaml. Default: test.yaml')
subparsers = parser.add_subparsers(dest='cmd')
subparser_editor = subparsers.add_parser('edit', help=
    'Launches the editor to edit or create new systems and components')
subparser_run = subparsers.add_parser('run', help=
    'Launches the setup specified by the --config argument')
subparser_val = subparsers.add_parser('validate', help=
    'Validate the setup specified by the --config argument')
subparser_remote = subparsers.add_parser('slave', help=
    """Run a component locally without controlling it. The control is taken care of the remote master invoking this command.
If run with the --kill flag, the passed component will be killed"""
    )
subparser_val.add_argument('--visual', help=
    'Generate and show a graph image', action='store_true')
remote_mutex = subparser_remote.add_mutually_exclusive_group(required=False)
remote_mutex.add_argument('-k', '--kill', help='switch to kill mode',
    action='store_true')
remote_mutex.add_argument('-c', '--check', help='Run a component check',
    action='store_true')
args = parser.parse_args()
logger.debug(args)
if args.cmd == 'edit':
logger.debug('Launching editor mode')
if args.cmd == 'run':
logger.debug('Launching runner mode')
if args.cmd == 'validate':
cc = ControlCenter(args.config)
logger.debug('Launching validation mode')
if args.cmd == 'slave':
cc.init()
cc = ControlCenter(args.config)
logger.debug('Launching slave mode')
start_gui(cc)
if args.visual:
sl = SlaveLauncher(args.config, args.kill, args.check)
cc.set_dependencies(False)
cc.set_dependencies(True)
if args.check:
cc.draw_graph()
sl.run_check()
sl.init()
