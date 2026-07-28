def get_competence_acl(self):...
"""docstring"""
acl = DEFAULT_PERM[:]
login = self.contractor.login
acl.append((Allow, u'%s' % login, ('view_competence', 'edit_competence')))
return acl
