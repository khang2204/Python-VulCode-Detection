@property...
if os.path.exists(self._osx_java_home_exe):
plist = subprocess.check_output([self._osx_java_home_exe, '--failfast',
    '--xml'])
plist_results = plistlib.loads(plist) if PY3 else plistlib.readPlistFromString(
    plist)
for distribution in plist_results:
home = distribution['JVMHomePath']
yield self.Location.from_home(home)
