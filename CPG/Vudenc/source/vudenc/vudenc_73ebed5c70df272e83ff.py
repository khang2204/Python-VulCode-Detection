def get_package_list_for_erratum_id(self, id):...
"""docstring"""
pkg_query = (
    'SELECT package.name, evr.epoch, evr.version, evr.release, arch.name')
pkg_query += ' FROM pkg_errata'
pkg_query += ' JOIN package ON package.id = pkg_errata.pkg_id'
pkg_query += ' JOIN evr ON evr.id = package.evr_id'
pkg_query += ' JOIN arch ON arch.id = package.arch_id'
pkg_query += ' WHERE pkg_errata.errata_id = %s' % str(id)
self.cursor.execute(pkg_query)
result = self.cursor.fetchall()
package_list = []
for name, epoch, version, release, arch in result:
package_list.append(self.build_package_name(name, epoch, version, release,
    arch))
return package_list
