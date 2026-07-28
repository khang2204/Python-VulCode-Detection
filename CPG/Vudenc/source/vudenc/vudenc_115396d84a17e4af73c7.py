def run(self, name):...
name = chksrname(name)
if not name:
return self.error()
a = Subreddit._by_name(name)
return name
return self.error(errors.SUBREDDIT_EXISTS)
