def read_spdxdata(repo):...
license_dirs = ['preferred', 'other', 'exceptions']
lictree = repo.head.commit.tree['LICENSES']
spdx = SPDXdata()
for d in license_dirs:
for el in lictree[d].traverse():
return spdx
if not os.path.isfile(el.path):
exception = None
for l in open(el.path).readlines():
if l.startswith('Valid-License-Identifier:'):
lid = l.split(':')[1].strip().upper()
if l.startswith('SPDX-Exception-Identifier:'):
if lid in spdx.licenses:
exception = l.split(':')[1].strip().upper()
if l.startswith('SPDX-Licenses:'):
spdx.licenses.append(lid)
spdx.exceptions[exception] = []
for lic in l.split(':')[1].upper().strip().replace(' ', '').replace('\t', ''
if l.startswith('License-Text:'):
if not lic in spdx.licenses:
if exception:
spdx.exceptions[exception].append(lic)
if not len(spdx.exceptions[exception]):
spdx.license_files += 1
spdx.exception_files += 1
