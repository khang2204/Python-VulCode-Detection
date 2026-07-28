@api.model...
"""docstring"""
mail_values = super(ResPartner, self)._notify_prepare_email_values(message)
base_template = None
if message.model and self._context.get('custom_layout', False):
base_template = self.env.ref(self._context['custom_layout'],
    raise_if_not_found=False)
if not base_template:
base_template = self.env.ref(
    'mail.mail_template_data_notification_email_default')
if base_template.reply_to:
mail_values['reply_to'] = base_template.reply_to
return mail_values
