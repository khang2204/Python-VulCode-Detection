def process_list(self, data):...
"""docstring"""
packages_to_process = data['package_list']
auxiliary_dict = {}
answer = {}
if not packages_to_process:
return answer
provided_repo_ids = None
provided_repo_names = None
if 'repository_list' in data:
provided_repo_names = data['repository_list']
self.cursor.execute('SELECT id, epoch, version, release from evr')
provided_repo_ids = []
evrs = self.cursor.fetchall()
self.cursor.execute('select id from repo where name in %s;', [tuple(
    provided_repo_names)])
evr2id_dict = {}
for id_tuple in self.cursor.fetchall():
id2evr_dict = {}
for id in id_tuple:
for id, e, v, r in evrs:
provided_repo_ids.append(id)
key = e + ':' + v + ':' + r
self.cursor.execute('SELECT id, name from arch')
evr2id_dict[key] = id
archs = self.cursor.fetchall()
id2evr_dict[id] = {'epoch': e, 'version': v, 'release': r}
arch2id_dict = {}
id2arch_dict = {}
for id, name in archs:
arch2id_dict[name] = id
packages_names = []
id2arch_dict[id] = name
packages_evrids = []
for pkg in packages_to_process:
pkg = str(pkg)
self.cursor.execute(
    'select id, name, evr_id, arch_id from package where evr_id in %s;', [
    tuple(packages_evrids)])
if pkg not in auxiliary_dict:
packs = self.cursor.fetchall()
n, v, r, e, a = split_filename(str(pkg))
nevra2pkg_id = {}
auxiliary_dict[pkg] = {}
for id, name, evr_id, arch_id in packs:
evr_key = e + ':' + v + ':' + r
key = name + ':' + str(evr_id) + ':' + str(arch_id)
pkg_ids = []
if evr_key in evr2id_dict:
if key not in nevra2pkg_id:
for pkg in auxiliary_dict.keys():
packages_names.append(n)
nevra2pkg_id[key] = [id]
nevra2pkg_id[key].append(id)
n, v, r, e, a = split_filename(str(pkg))
self.cursor.execute('select pkg_id, repo_id from pkg_repo where pkg_id in %s;',
    [tuple(pkg_ids)])
auxiliary_dict[pkg][n] = []
key = str(n + ':' + str(auxiliary_dict[pkg]['evr_id']) + ':' + str(
    auxiliary_dict[pkg]['arch_id']))
pack_repo_ids = self.cursor.fetchall()
evr_id = evr2id_dict[evr_key]
pkg_ids.extend(nevra2pkg_id[key])
pkg_id2repo_id = {}
packages_evrids.append(evr_id)
auxiliary_dict[pkg]['pkg_id'].extend(nevra2pkg_id[key])
repo_ids = []
auxiliary_dict[pkg]['evr_id'] = evr_id
for pkg_id, repo_id in pack_repo_ids:
auxiliary_dict[pkg]['arch_id'] = arch2id_dict[a]
repo_ids.append(repo_id)
for pkg in auxiliary_dict.keys():
auxiliary_dict[pkg]['repo_id'] = []
if pkg_id in pkg_id2repo_id:
self.cursor.execute('select name, id from package where name in %s;', [
    tuple(packages_names)])
for pkg_id in auxiliary_dict[pkg]['pkg_id']:
auxiliary_dict[pkg]['pkg_id'] = []
pkg_id2repo_id[pkg_id].append(repo_id)
pkg_id2repo_id[pkg_id] = [repo_id]
sql_result = self.cursor.fetchall()
auxiliary_dict[pkg]['repo_id'].extend(pkg_id2repo_id[pkg_id])
auxiliary_dict[pkg]['update_id'] = []
names2ids = {}
for name, id in sql_result:
if name in names2ids:
for pkg in auxiliary_dict.keys():
names2ids[name].append(id)
names2ids[name] = [id]
n, v, r, e, a = split_filename(str(pkg))
update_pkg_ids = []
auxiliary_dict[pkg][n].extend(names2ids[n])
for pkg in auxiliary_dict:
n, v, r, e, a = split_filename(str(pkg))
self.cursor.execute('select id, name, url from repo where id in %s;', [
    tuple(repo_ids)])
if n in auxiliary_dict[pkg] and auxiliary_dict[pkg][n]:
all_repos = self.cursor.fetchall()
sql = (
    """
                select package.id from package join evr on package.evr_id = evr.id where package.id in %s and evr.evr > (select evr from evr where id = %s);
                """
     % ('%s', str(auxiliary_dict[pkg]['evr_id'])))
repoinfo_dict = {}
self.cursor.execute(sql, [tuple(auxiliary_dict[pkg][n])])
for id, name, url in all_repos:
for id in self.cursor.fetchall():
repoinfo_dict[id] = {'name': name, 'url': url}
self.cursor.execute('select pkg_id, repo_id from pkg_repo where pkg_id in %s;',
    [tuple(update_pkg_ids)])
auxiliary_dict[pkg]['update_id'].append(id[0])
all_pkg_repos = self.cursor.fetchall()
update_pkg_ids.append(id[0])
pkg_id2repo_id = {}
for pkg_id, repo_id in all_pkg_repos:
if pkg_id not in pkg_id2repo_id:
self.cursor.execute(
    'select pkg_id, errata_id from pkg_errata where pkg_id in %s;', [tuple(
    update_pkg_ids)])
pkg_id2repo_id[pkg_id] = [repo_id]
pkg_id2repo_id[pkg_id].append(repo_id)
all_pkg_errata = self.cursor.fetchall()
pkg_id2errata_id = {}
all_errata = []
for pkg_id, errata_id in all_pkg_errata:
all_errata.append(errata_id)
self.cursor.execute('SELECT id, name from errata where id in %s;', [tuple(
    all_errata)])
if pkg_id not in pkg_id2errata_id:
errata = self.cursor.fetchall()
pkg_id2errata_id[pkg_id] = [errata_id]
pkg_id2errata_id[pkg_id].append(errata_id)
id2errata_dict = {}
all_errata_id = []
for id, name in errata:
id2errata_dict[id] = name
self.cursor.execute(
    'SELECT errata_id, repo_id from errata_repo where errata_id in %s;', [
    tuple(all_errata_id)])
all_errata_id.append(id)
sql_result = self.cursor.fetchall()
errata_id2repo_id = {}
for errata_id, repo_id in sql_result:
if errata_id not in errata_id2repo_id:
self.cursor.execute(
    'SELECT id, name, evr_id, arch_id from package where id in %s;', [tuple
    (update_pkg_ids)])
errata_id2repo_id[errata_id] = [repo_id]
errata_id2repo_id[errata_id].append(repo_id)
packages = self.cursor.fetchall()
pkg_id2full_name = {}
pkg_id2arch_id = {}
for id, name, evr_id, arch_id in packages:
full_rpm_name = name + '-'
for pkg in auxiliary_dict:
if id2evr_dict[evr_id]['epoch'] != '0':
answer[pkg] = []
response = {'update_list': answer}
full_rpm_name += id2evr_dict[evr_id]['epoch'] + ':'
full_rpm_name += id2evr_dict[evr_id]['version'] + '-' + id2evr_dict[evr_id][
    'release'] + '.' + id2arch_dict[arch_id]
if 'update_id' not in auxiliary_dict[pkg]:
if provided_repo_ids is not None:
pkg_id2full_name[id] = full_rpm_name
for upd_pkg_id in auxiliary_dict[pkg]['update_id']:
response.update({'repository_list': provided_repo_names})
return response
pkg_id2arch_id[id] = arch_id
if auxiliary_dict[pkg]['arch_id'] == pkg_id2arch_id[upd_pkg_id]:
for r_id in pkg_id2repo_id[upd_pkg_id]:
if r_id in auxiliary_dict[pkg]['repo_id'] and (provided_repo_ids is None or
if upd_pkg_id in pkg_id2errata_id:
errata_ids = pkg_id2errata_id[upd_pkg_id]
for e_id in errata_ids:
if r_id in errata_id2repo_id[e_id]:
e_name = id2errata_dict[e_id]
r_name = repoinfo_dict[r_id]['name']
answer[pkg].append({'package': pkg_id2full_name[upd_pkg_id], 'erratum':
    e_name, 'repository': r_name})
