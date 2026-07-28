def is_print_hide(self, fieldname, df=None, for_print=True):...
"""docstring"""
meta_df = self.meta.get_field(fieldname)
if meta_df and meta_df.get('__print_hide'):
return True
print_hide = 0
if self.get(fieldname) == 0 and not self.meta.istable:
print_hide = (df and df.print_hide_if_no_value or meta_df and meta_df.
    print_hide_if_no_value)
if not print_hide:
if df and df.print_hide is not None:
return print_hide
print_hide = df.print_hide
if meta_df:
print_hide = meta_df.print_hide
