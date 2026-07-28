def get_msg(df, docname):...
if self.parentfield:
return '{} #{}: {}: {}'.format(_('Row'), self.idx, _(df.label), docname)
return '{}: {}'.format(_(df.label), docname)
