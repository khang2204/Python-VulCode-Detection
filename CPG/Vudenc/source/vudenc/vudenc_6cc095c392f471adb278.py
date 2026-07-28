@transaction.atomic...
form = RegisterStudentForm(request.POST)
if not form.is_valid():
return make_view(request, register_student_form=form)
course = Course.objects.get(course_number=request.POST['course_number'])
student = Student.objects.get(andrew_id=request.POST['andrew_id'])
course.students.add(student)
course.save()
return make_view(request, messages=['Added %s to %s' % (student, course)])
