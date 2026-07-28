@script('up')...
argument_parser = argparse.ArgumentParser('Website')
argument_parser.add_argument('purpose', help='which website to bring up')
argument_parser.add_argument('--dependency', type=str, help=
    'where @periodic_job is defined', nargs='+', dest='dependencies')
args = argument_parser.parse_args(argv)
for dependency in args.dependencies:
__import__(dependency)
start_website(args.purpose)
