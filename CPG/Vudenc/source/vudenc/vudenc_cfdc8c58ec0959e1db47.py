import argparse, sys, tld
import urllib.parse, os
from files import config
from core.colors import R, G
from core.updater import updater
parser = argparse.ArgumentParser('python3 xsrfprobe.py')
parser._action_groups.pop()
required = parser.add_argument_group('Required Arguments')
optional = parser.add_argument_group('Optional Arguments')
required.add_argument('-u', '--url', help='Main URL to test', dest='url')
optional.add_argument('-c', '--cookie', help=
    'Cookie value to be requested with each successive request. If there are multiple cookies, separate them with commas. For example: `-c PHPSESSID=i837c5n83u4, _gid=jdhfbuysf`.'
    , dest='cookie')
optional.add_argument('-o', '--output', help=
    'Output directory where files to be stored. Default is the`files` folder where all files generated will be stored.'
    , dest='output')
optional.add_argument('-d', '--delay', help=
    'Time delay between requests in seconds. Default is zero.', dest=
    'delay', type=float)
optional.add_argument('-q', '--quiet', help=
    'Set the DEBUG mode to quiet. Report only when vulnerabilities are found. Minimal output will be printed on screen. '
    , dest='quiet', action='store_true')
optional.add_argument('-v', '--verbose', help=
    'Increase the verbosity of the output (e.g., -vv is more than -v). ',
    dest='verbose', action='store_true')
optional.add_argument('--user-agent', help=
    'Custom user-agent to be used. Only one user-agent can be specified.',
    dest='user_agent', type=str)
optional.add_argument('--headers', help=
    'Comma separated list of custom headers you\'d want to use. For example: ``--headers "Accept=text/php, X-Requested-With=Dumb"``.'
    , dest='headers', type=str)
optional.add_argument('--exclude', help=
    "Comma separated list of paths or directories to be excluded which are not in scope. These paths/dirs won't be scanned. For example: `--exclude somepage/, sensitive-dir/, pleasedontscan/`"
    , dest='exclude', type=str)
optional.add_argument('--timeout', help=
    'HTTP request timeout value in seconds. The entered value must be in floating point decimal. Example: ``--timeout 10.0``'
    , dest='timeout', type=float)
optional.add_argument('--max-chars', help=
    'Maximum allowed character length for the custom token value to be generated. For example: `--max-chars 5`. Default value is 6.'
    , dest='maxchars', type=int)
optional.add_argument('--crawl', help=
    'Crawl the whole site and simultaneously test all discovered endpoints for CSRF.'
    , dest='crawl', action='store_true')
optional.add_argument('--skip-analysis', help=
    'Skip the Post-Scan Analysis of Tokens which were gathered during requests'
    , dest='skipal', action='store_true')
optional.add_argument('--skip-poc', help=
    'Skip the PoC Form Generation of POST-Based Cross Site Request Forgeries.',
    dest='skippoc', action='store_true')
optional.add_argument('--update', help=
    'Update XSRFProbe to latest version on GitHub via git.', dest='update',
    action='store_true')
optional.add_argument('--random-agent', help=
    'Use random user-agents for making requests.', dest='randagent', action
    ='store_true')
optional.add_argument('--version', help=
    'Display the version of XSRFProbe and exit.', dest='version', action=
    'store_true')
args = parser.parse_args()
if not len(sys.argv) > 1:
print(
    """
    [1;91mXSRFProbe[0m, [1;97mA [1;93mCross Site Request Forgery [1;97mAudit Toolkit[0m
"""
    )
if args.update:
parser.print_help()
updater()
if args.version:
quit('')
quit('')
print("""
[1;97m [+] [1;91mXSRFProbe Version[0m : [1;97m""" + open(
    'files/VersionNum').read())
if args.maxchars:
quit()
config.TOKEN_GENERATION_LENGTH = args.maxchars
if args.user_agent:
config.USER_AGENT = args.user_agent
if args.skipal:
config.SCAN_ANALYSIS = False
if args.skippoc:
config.POC_GENERATION = False
if not args.version and not args.update:
if args.url:
if args.crawl:
if 'http' in args.url:
print(R + 'You must supply a url/endpoint.')
config.CRAWL_SITE = True
if args.cookie:
config.SITE_URL = args.url
config.SITE_URL = 'http://' + args.url
if ',' in args.cookie:
if args.timeout:
for cook in args.cookie.split(','):
config.TIMEOUT_VALUE = args.timeout
if args.headers:
config.COOKIE_VALUE.append(cook.strip())
for m in args.headers.split(','):
if args.exclude:
config.USER_AGENT_RANDOM = False
config.HEADER_VALUES[m.split('=')[0]] = m.split('=')[1]
exc = args.exclude
if args.randagent:
m = exc.split(',').strip()
config.USER_AGENT_RANDOM = True
if config.SITE_URL:
for s in m:
config.USER_AGENT = ''
if args.output:
if args.quiet:
config.EXCLUDE_DIRS.append(urllib.parse.urljoin(config.SITE_URL, s))
if not os.path.exists(args.output + tld.get_fld(config.SITE_URL)):
config.OUTPUT_DIR = args.output + tld.get_fld(config.SITE_URL) + '/'
os.makedirs(tld.get_fld(config.SITE_URL))
config.OUTPUT_DIR = tld.get_fld(config.SITE_URL) + '/'
config.DEBUG = False
os.makedirs(args.output + tld.get_fld(config.SITE_URL))
