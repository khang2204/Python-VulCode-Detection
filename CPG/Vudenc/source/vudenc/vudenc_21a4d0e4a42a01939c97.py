def run(self, limit):...
if limit is None:
return c.user.pref_numsites
return min(max(int(limit), 1), 250)
