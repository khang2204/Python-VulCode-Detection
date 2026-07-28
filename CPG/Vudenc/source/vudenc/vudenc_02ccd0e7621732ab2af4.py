def package(manifest, pkg, target):...
"""docstring"""
version = manifest['pkg'][pkg]['version']
info = manifest['pkg'][pkg]['target'][target]
return version, info
