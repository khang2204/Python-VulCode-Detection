def run(self, url, sr=None):...
if sr is None and not isinstance(c.site, FakeSubreddit):
sr = c.site
if sr:
if not url:
sr = None
sr = Subreddit._by_name(sr)
c.errors.add(errors.SUBREDDIT_NOEXIST)
return self.error(errors.NO_URL)
url = utils.sanitize_url(url)
sr = None
if url == 'self':
return url
if url:
l = Link._by_url(url, sr)
return url
return self.error(errors.BAD_URL)
self.error(errors.ALREADY_SUB)
return utils.tup(l)
