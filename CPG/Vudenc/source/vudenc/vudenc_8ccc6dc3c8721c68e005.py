def get_form(self, request, obj=None, **kwargs):...
"""docstring"""
if obj is None:
return super(CheckCVEAdmin, self).get_form(request, obj, **kwargs)
return CheckCVEChangeForm
