def formfield(self, **kwargs):...
from common.forms import JsonField
defaults = {'form_class': JsonField}
defaults.update(kwargs)
return super().formfield(**defaults)
