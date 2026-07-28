def one_to_one_check(self, odict):...
"""docstring"""
if hasattr(self, 'cat_code'):
return self.cat_code != odict['cat_code']
return self.prod_name != odict['prod_name']
