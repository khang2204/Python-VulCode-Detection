def send_email(context_data, from_email, to_email, template_subject,...
"""docstring"""
context = Context(context_data)
subj_template = loader.get_template(template_subject)
rendered_subj = subj_template.render(context)
text_template = loader.get_template(template_text)
rendered_text = text_template.render(context)
send_mail(rendered_subj, rendered_text, from_email, to_email, fail_silently
    =True)
