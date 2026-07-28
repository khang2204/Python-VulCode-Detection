@staticmethod...
"""docstring"""
package_name = name + '-'
if int(epoch) > 0:
package_name += '%s:' % epoch
package_name += '%s-%s.%s' % (version, release, arch)
return package_name
