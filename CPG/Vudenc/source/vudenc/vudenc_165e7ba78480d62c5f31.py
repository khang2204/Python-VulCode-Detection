def get_file_acl(self):...
"""docstring"""
if self.parent is not None:
return self.parent.__acl__
if self.company_header_backref is not None:
return self.company_header_backref.__acl__
if self.company_logo_backref is not None:
return self.company_logo_backref.__acl__
return []
