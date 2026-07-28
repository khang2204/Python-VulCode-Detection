"""
Various utilities.
"""
import functools
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader, Context
from core.common.mongo import c_onboarding_status, c_onboarding_settings
from core.common import onboarding
def send_email(context_data, from_email, to_email, template_subject,...
"""docstring"""
context = Context(context_data)
subj_template = loader.get_template(template_subject)
rendered_subj = subj_template.render(context)
text_template = loader.get_template(template_text)
rendered_text = text_template.render(context)
send_mail(rendered_subj, rendered_text, from_email, to_email, fail_silently
    =True)
def suspending_receiver(signal, **decorator_kwargs):...
"""docstring"""
def our_wrapper(func):...
@receiver(signal, **decorator_kwargs)...
if settings.SUSPEND_SIGNALS:
return
return func(sender, **kwargs)
