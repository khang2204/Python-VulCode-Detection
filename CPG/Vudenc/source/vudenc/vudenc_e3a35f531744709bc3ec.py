def _sendmail(self):...
mail_context = TestCase.mail_scene(objects=self._update_objects, field=self
    .target_field, value=self.new_value)
if mail_context:
from tcms.core.utils.mailto import mailto
mail_context['context']['user'] = self.request.user
mailto(**mail_context)
