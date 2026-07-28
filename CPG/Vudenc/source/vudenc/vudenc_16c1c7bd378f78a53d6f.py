@transaction.atomic...
form = CreateCourseForm(request.POST)
if not form.is_valid():
return make_view(request, create_course_form=form)
new_course = Course(course_number=request.POST['course_number'],
    course_name=request.POST['course_name'], instructor=request.POST[
    'instructor'])
new_course.save()
return make_view(request, messages=['Added %s' % new_course])
