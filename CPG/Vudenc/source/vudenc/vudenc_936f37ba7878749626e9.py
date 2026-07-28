def main():...
log_file = dglogger.log_config()
dglogger.log_start()
parser = argparse.ArgumentParser(description=
    """install_mac_tweaks changes user and global settings to improve performance, security, 
    and convenience. Results logged to a file."""
    )
group = parser.add_mutually_exclusive_group()
group.add_argument('--mode', choices=['b', 'batch', 'i', 'interactive'],
    action='store', default='batch', help=
    'Run interactively to confirm each change.')
group.add_argument('--list', choices=['all', 'a', 'groups', 'g',
    'descriptions', 'd'], action='store', help=
    'Print lists of the groups and set commands. Silently ignores --groups.')
parser.add_argument('--groups', type=str, nargs='+', help=
    'Select a subset of tweaks to execute')
args = parser.parse_args()
import tweaks
dglogger.log_error(e, file=sys.stderr)
if args.list is not None:
dglogger.log_end(log_file)
run_list_mode()
if args.mode == 'batch' or args.mode == 'b':
sys.exit(1)
sys.exit(0)
run_batch_mode(tweaks.tweaks, args)
if args.mode == 'interactive' or args.mode == 'i':
dglogger.log_end(log_file)
run_interactive_mode()
