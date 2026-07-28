def get_onboarding_percentage(user_id):...
if user_id:
status = c_onboarding_status(use_secondary=True).find_one({onboarding.
    USER_ID: user_id}) or {}
return 0
if status:
steps = [status.get(key, False) for key in get_onboarding_steps()]
return round(len(filter(lambda x: x, steps)) / float(len(steps)) * 100, 0)
