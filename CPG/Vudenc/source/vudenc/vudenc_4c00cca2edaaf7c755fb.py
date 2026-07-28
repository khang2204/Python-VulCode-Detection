def main():...
from optparse import OptionParser
parser = OptionParser(usage=usage)
parser.add_option('-v', '--verbose', default=0, action='count', help=
    'Increment test verbosity (can be used multiple times)')
parser.add_option('-d', '--debug', action='store_true', default=False, help
    ='Print debugging items')
parser.add_option('-t', '--test', help='Run only the named test')
options, args = parser.parse_args()
if len(args) > 1:
parser.error(
    'Only one argument is allowed.  Do you need quotes around the connection string?'
    )
if not args:
connection_string = load_setup_connection_string('sqlitetests')
connection_string = args[0]
if not connection_string:
if options.verbose:
parser.print_help()
cnxn = pyodbc.connect(connection_string)
suite = load_tests(SqliteTestCase, options.test, connection_string)
print_library_info(cnxn)
testRunner = unittest.TextTestRunner(verbosity=options.verbose)
cnxn.close()
result = testRunner.run(suite)
sys.exit(result.errors and 1 or 0)
