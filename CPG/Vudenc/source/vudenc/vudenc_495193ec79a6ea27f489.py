def redirections(self):...
redirs = []
redir = self.redirection()
while redir:
redirs.append(redir)
if len(redirs) > 0:
redir = self.redirection()
return RedirectionsHelper(redirs)
return None
