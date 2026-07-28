def get_onboarding_status_with_settings(user_id):...
"""docstring"""
onboarding_status = c_onboarding_status().find_one({onboarding.USER_ID:
    user_id}, {'_id': 0, 'user_id': 0}) or {}
data = {}
for step in get_onboarding_steps():
data[step] = {'done': onboarding_status.get(step, False)}
return data
