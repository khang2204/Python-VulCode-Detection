def make_view(request, messages=[], create_student_form=CreateStudentForm(),...
context = {'courses': Course.objects.all(), 'messages': messages,
    'create_student_form': create_student_form, 'create_course_form':
    create_course_form, 'register_student_form': register_student_form}
return render(request, 'sio.html', context)
