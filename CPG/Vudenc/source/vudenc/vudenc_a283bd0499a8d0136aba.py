import collections
import itertools
import reframe as rfm
from reframe.core.exceptions import DependencyError
def build_deps(cases):...
"""docstring"""
cases_by_part = {}
cases_revmap = {}
for c in cases:
cname = c.check.name
def resolve_dep(target, from_map, *args):...
pname = c.partition.fullname
errmsg = 'could not resolve dependency: %s' % target
ename = c.environ.name
ret = from_map[args]
if not ret:
graph = {}
cases_by_part.setdefault((cname, pname), [])
return ret
for c in cases:
cases_revmap.setdefault((cname, pname, ename), None)
graph[c] = c.deps
return graph
cases_by_part[cname, pname].append(c)
cname = c.check.name
cases_revmap[cname, pname, ename] = c
pname = c.partition.fullname
ename = c.environ.name
for dep in c.check.user_deps():
tname, how, subdeps = dep
if how == rfm.DEPEND_FULLY:
c.deps.extend(resolve_dep(c, cases_by_part, tname, pname))
if how == rfm.DEPEND_BY_ENV:
c.deps.append(resolve_dep(c, cases_revmap, tname, pname, ename))
if how == rfm.DEPEND_EXACT:
for env, tenvs in subdeps.items():
if env != ename:
for te in tenvs:
c.deps.append(resolve_dep(c, cases_revmap, tname, pname, te))
