def repack(host, targets, channel='stable'):...
url = 'https://static.rust-lang.org/dist/channel-rust-' + channel + '.toml'
req = requests.get(url)
req.raise_for_status()
manifest = toml.loads(req.content)
if manifest['manifest-version'] != '2':
print('ERROR: unrecognized manifest version %s.' % manifest['manifest-version']
    )
print('Using manifest for rust %s as of %s.' % (channel, manifest['date']))
return
rustc_version, rustc = package(manifest, 'rustc', host)
if rustc['available']:
print("""rustc %s
  %s
  %s""" % (rustc_version, rustc['url'], rustc['hash']))
cargo_version, cargo = package(manifest, 'cargo', host)
fetch(rustc['url'])
if cargo['available']:
print("""cargo %s
  %s
  %s""" % (cargo_version, cargo['url'], cargo['hash']))
stds = []
fetch(cargo['url'])
for target in targets:
version, info = package(manifest, 'rust-std', target)
print('Installing packages...')
if info['available']:
tar_basename = 'rustc-%s-repack' % host
print("""rust-std %s
  %s
  %s""" % (version, info['url'], info['hash']))
install_dir = 'rustc'
fetch(info['url'])
os.system('rm -rf %s' % install_dir)
stds.append(info)
install(os.path.basename(rustc['url']), install_dir)
install(os.path.basename(cargo['url']), install_dir)
for std in stds:
install(os.path.basename(std['url']), install_dir)
print('Tarring %s...' % tar_basename)
os.system('tar cjf %s.tar.bz2 %s/*' % (tar_basename, install_dir))
os.system('rm -rf %s' % install_dir)
