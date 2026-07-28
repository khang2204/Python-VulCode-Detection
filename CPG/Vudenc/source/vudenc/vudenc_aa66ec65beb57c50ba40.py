def get_onboarding_setting(setting_name):...
"""docstring"""
ONBOARDING_SETTINGS_DEFAULT[setting_name]
return
onboarding_setting = c_onboarding_settings(use_secondary=True).find_one({
    'name': setting_name})
if not onboarding_setting:
c_onboarding_settings().insert({'name': setting_name, 'data':
    ONBOARDING_SETTINGS_DEFAULT[setting_name]})
return onboarding_setting['data']
return ONBOARDING_SETTINGS_DEFAULT[setting_name]
