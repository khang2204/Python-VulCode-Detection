def parse_opts(argv):...
parser = argparse.ArgumentParser(description=
    'Reads and merges JSON configuration files specified by colon separated environment variable OS_CONFIG_FILES, unless overridden by command line option --metadata. If no files are specified this way, falls back to legacy behavior of searching the fallback metadata path for a single config file.'
    )
parser.add_argument('-t', '--templates', metavar='TEMPLATE_ROOT', help=
    """path to template root directory (default:
                        %(default)s)"""
    , default=TEMPLATES_DIR)
parser.add_argument('-o', '--output', metavar='OUT_DIR', help=
    'root directory for output (default:%(default)s)', default='/')
parser.add_argument('-m', '--metadata', metavar='METADATA_FILE', nargs='*',
    help=
    'Overrides environment variable OS_CONFIG_FILES. Specify multiple times, rather than separate files with ":".'
    , default=[])
parser.add_argument('--fallback-metadata', metavar='FALLBACK_METADATA',
    nargs='*', help=
    'Files to search when OS_CONFIG_FILES is empty. (default: %(default)s)',
    default=['/var/cache/heat-cfntools/last_metadata',
    '/var/lib/heat-cfntools/cfn-init-data',
    '/var/lib/cloud/data/cfn-init-data'])
parser.add_argument('-v', '--validate', help=
    'validate only. do not write files', default=False, action='store_true')
parser.add_argument('--print-templates', default=False, action='store_true',
    help='Print templates root and exit.')
parser.add_argument('-s', '--subhash', help=
    'use the sub-hash named by this key, instead of the full metadata hash')
parser.add_argument('--key', metavar='KEY', default=None, help=
    'print the specified key and exit. (may be used with --type and --key-default)'
    )
parser.add_argument('--type', default='default', help=
    'exit with error if the specified --key does not match type. Valid types are <int|default|netaddress|netdevice|dsn|swiftdevices|raw>'
    )
parser.add_argument('--key-default', help=
    'This option only affects running with --key. Print this if key is not found. This value is not subject to type restrictions. If --key is specified and no default is specified, program exits with an error on missing key.'
    )
parser.add_argument('--version', action='version', version=version.
    version_info.version_string())
parser.add_argument('--os-config-files', default=OS_CONFIG_FILES_PATH, help
    ='Set path to os_config_files.json')
opts = parser.parse_args(argv[1:])
return opts
