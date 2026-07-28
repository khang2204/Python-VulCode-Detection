def update_context_for_enterprise(request, context):...
"""docstring"""
context = context.copy()
sidebar_context = enterprise_sidebar_context(request)
if sidebar_context:
context['data']['registration_form_desc']['fields'] = enterprise_fields_only(
    context['data']['registration_form_desc'])
context['enable_enterprise_sidebar'] = False
context.update(sidebar_context)
return context
context['enable_enterprise_sidebar'] = True
context['data']['hide_auth_warnings'] = True
