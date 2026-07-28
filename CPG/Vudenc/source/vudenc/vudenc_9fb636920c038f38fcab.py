def get_targets(self):...
found_count = 0
for user, forum in self.forums:
targets = []
return found_count
self.log.debug('Scanning first page of the forum %s:%s', user, forum)
page = self.site.get_page('1', forum, user)
rxp = re.compile(regexp.f_sub_id.format(user, self.site.domain, forum))
found = set(map(lambda x: (user, x[0] + x[1]), rxp.findall(page)))
for t in found:
if t in self.pc.sets['closed'] or t in self.pc.sets['bumplimit'
lt = len(targets)
targets.append(t)
found_count += lt
if lt > 0:
self.log.info('Found %d new targets in forum %s:%s', lt, user, forum)
self.log.debug('Found no new targets in forum %s:%s', user, forum)
self.targets.extend(targets)
