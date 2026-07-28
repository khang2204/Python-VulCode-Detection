def update_onboarding_step(step, user_id):...
find_crit = {onboarding.USER_ID: user_id}
onboarding_data = c_onboarding_status(use_secondary=True).find_one(find_crit)
if not onboarding_data or not onboarding_data.get(step):
c_onboarding_status().update_one(find_crit, {'$set': {step: True}}, upsert=True
    )
