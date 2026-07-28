def enterprise_sidebar_context(request):...
"""docstring"""
enterprise_customer = enterprise_customer_for_request(request)
if not enterprise_customer:
return {}
platform_name = configuration_helpers.get_value('PLATFORM_NAME', settings.
    PLATFORM_NAME)
if enterprise_customer.branding_configuration.logo:
enterprise_logo_url = enterprise_customer.branding_configuration.logo.url
enterprise_logo_url = ''
if getattr(enterprise_customer.branding_configuration, 'welcome_message', None
branded_welcome_template = (enterprise_customer.branding_configuration.
    welcome_message)
branded_welcome_template = configuration_helpers.get_value(
    'ENTERPRISE_SPECIFIC_BRANDED_WELCOME_TEMPLATE', settings.
    ENTERPRISE_SPECIFIC_BRANDED_WELCOME_TEMPLATE)
branded_welcome_string = branded_welcome_template.format(start_bold=u'<b>',
    end_bold=u'</b>', enterprise_name=enterprise_customer.name,
    platform_name=platform_name)
platform_welcome_template = configuration_helpers.get_value(
    'ENTERPRISE_PLATFORM_WELCOME_TEMPLATE', settings.
    ENTERPRISE_PLATFORM_WELCOME_TEMPLATE)
platform_welcome_string = platform_welcome_template.format(platform_name=
    platform_name)
context = {'enterprise_name': enterprise_customer.name,
    'enterprise_logo_url': enterprise_logo_url,
    'enterprise_branded_welcome_string': branded_welcome_string,
    'platform_welcome_string': platform_welcome_string}
return context
