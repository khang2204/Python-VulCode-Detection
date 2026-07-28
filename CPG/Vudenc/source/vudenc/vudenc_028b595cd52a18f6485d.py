def handle(self, *args, **options):...
for instructor in Instructor.objects.all():
course = Course.objects.get(id=settings.ONBOARDING_INTRODUCTION_COURSE_ID)
print('Onboarding course is not provided')
chat_exists = Chat.objects.filter(user=instructor.user,
    enroll_code__courseUnit__course=course, progress__gte=70).exists()
return
if chat_exists:
update_onboarding_step(onboarding.STEP_2, instructor.user_id)
if Course.objects.filter(addedBy=instructor.user).exists():
update_onboarding_step(onboarding.STEP_3, instructor.user_id)
if Unit.objects.filter(addedBy=instructor.user).exists():
update_onboarding_step(onboarding.STEP_4, instructor.user_id)
if Lesson.objects.filter(addedBy=instructor.user).exists():
update_onboarding_step(onboarding.STEP_5, instructor.user_id)
if Invite.objects.filter(instructor=instructor).exists():
update_onboarding_step(onboarding.STEP_8, instructor.user_id)
enroll_unit_code_exists = EnrollUnitCode.objects.filter(
    courseUnit__course__addedBy=instructor.user, isPreview=True, isLive=
    False, isTest=False).exists()
if enroll_unit_code_exists:
update_onboarding_step(onboarding.STEP_6, instructor.user_id)
print('Instructor {} passed onboarding at {}%'.format(instructor.user.
    username, get_onboarding_percentage(instructor.user.id)))
