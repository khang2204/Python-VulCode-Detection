@skip...
def mocked_setting(setting_name):...
data = {onboarding.INTRODUCTION_INTRO: {'html': '<p>instructor_intro</p>',
    'description': 'instructor_intro desc', 'title': 'instructor_intro'},
    onboarding.CREATE_COURSE: {'html': '<p>create_course</p>',
    'description': 'create_course desc', 'title': 'create_course'},
    onboarding.CREATE_COURSELET: {'html': '<p>create_courselet</p>',
    'description': 'create_courselet desc', 'title': 'create_courselet'},
    onboarding.NEXT_STEPS: {'html': '<p>next_steps</p>', 'description':
    'next_steps desc', 'title': 'next_steps'}, onboarding.INVITE_SOMEBODY:
    {'html': '<p>invite_somebody</p>', 'description':
    'invite_somebody desc', 'title': 'invite_somebody'}, onboarding.
    CREATE_THREAD: {'html': '<p>create_thread</p>', 'description':
    'create_thread desc', 'title': 'create_thread'}, onboarding.
    VIEW_INTRODUCTION: {'html': '<p>view_introduction</p>', 'description':
    'view_introduction desc', 'title': 'view_introduction'}, onboarding.
    PREVIEW_COURSELET: {'html': '<p>preview_courselet</p>', 'description':
    'preview_courselet desc', 'title': 'preview_courselet'}}
return data[setting_name]
