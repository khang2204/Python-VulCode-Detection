def install_deps(verbosity=False, dry_run=False, allow_daemons=True):...
errors = find_missing_deps()
if len(errors) == 0:
if verbosity:
missing_pkgs = []
sys.stderr.write('No missing dependencies\n')
return 0
for e in errors:
missing_pkgs += e.deps
deps_string = ' '.join(sorted(missing_pkgs))
if dry_run:
sys.stderr.write('Missing dependencies: %s\n' % deps_string)
if os.geteuid() != 0:
return 0
sys.stderr.write('Missing dependencies: %s\n' % deps_string)
if verbosity:
sys.stderr.write('Package installation is not possible as non-root.\n')
sys.stderr.write('Installing %s\n' % deps_string)
ret = 0
return 2
install_packages(missing_pkgs, allow_daemons=allow_daemons, aptopts=[
    '--no-install-recommends'])
sys.stderr.write('%s\n' % e)
return ret
ret = e.exit_code
