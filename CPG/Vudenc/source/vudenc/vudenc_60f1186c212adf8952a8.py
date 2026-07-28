def main(args):...
parser = optparse.OptionParser(description=sys.modules[__name__].__doc__)
parser.add_option('--in-file', help='Name of the request file')
parser.add_option('--out-file', help=
    'Name of the JSON file to write a task summary to')
parser.add_option('--swarming-server', help='Swarming server to send data back'
    )
parser.add_option('--cost-usd-hour', type='float', help=
    'Cost of this VM in $/h')
parser.add_option('--start', type='float', help='Time this task was started')
parser.add_option('--min-free-space', type='int', help=
    'Value to send down to run_isolated')
options, args = parser.parse_args(args)
if not options.in_file or not options.out_file or args:
parser.error('task_runner is meant to be used by swarming_bot.')
on_error.report_on_exception_exit(options.swarming_server)
logging.info('starting')
remote = xsrf_client.XsrfRemote(options.swarming_server)
now = monotonic_time()
if options.start > now:
options.start = now
load_and_run(options.in_file, remote, options.cost_usd_hour, options.start,
    options.out_file, options.min_free_space)
logging.info('quitting')
return 0
