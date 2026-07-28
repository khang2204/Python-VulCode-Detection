def run(self, fullname):...
thing = VByName.run(self, fullname)
if thing:
if not thing._loaded:
return self.error(errors.NOT_AUTHOR)
thing._load()
if c.user_is_loggedin and thing.author_id == c.user._id:
return thing
