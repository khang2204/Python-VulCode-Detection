def run(self, sort, where):...
if self.remember:
pref = '%s_%s' % (where, self.nav.get_param)
if sort not in self.nav.options:
user_prefs = copy(c.user.sort_options) if c.user else {}
sort = self.nav.default
if self.remember and c.user_is_loggedin and sort != user_pref:
user_pref = user_prefs.get(pref)
user_prefs[pref] = sort
return sort
if not sort:
c.user.sort_options = user_prefs
sort = user_pref
user = c.user
utils.worker.do(lambda : user._commit())
