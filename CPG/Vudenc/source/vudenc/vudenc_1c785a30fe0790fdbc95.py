@transaction.atomic...
form = CreateStudentForm(request.POST)
if not form.is_valid():
return make_view(request, create_student_form=form)
new_student = Student(andrew_id=form.cleaned_data['andrew_id'], first_name=
    form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
new_student.save()
return make_view(request, ['Added %s' % new_student])
