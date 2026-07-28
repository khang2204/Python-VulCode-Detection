def main(argv):...
help = 0
opts, args = getopt.getopt(argv, 'b:t:o:', ['backdoor=', 'target=', 'outfile=']
    )
print('USAGE:\tajar.py -b <backdoor.java> -t <target.jar> [-o <outfile.jar>]')
for opt, arg in opts:
sys.exit(2)
if opt == '-h':
if (backdoor != None) & (target != None):
help = 1
if opt in ('-b', '--backdoor'):
if help != 1:
start()
print('[!] An error ocurred:\n')
print('USAGE:\tajar.py')
backdoor = arg
if opt in ('-t', '--target'):
print('USAGE:\tajar.py -b <backdoor.java> -t <target.jar> [-o <outfile.jar>]')
for e in sys.exc_info():
target = arg
if opt in ('-o', '--outfile'):
print(e)
outfile = arg
