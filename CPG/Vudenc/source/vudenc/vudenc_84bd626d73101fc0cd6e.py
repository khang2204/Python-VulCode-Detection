def get_student_by_name(request):...
first_name = request.GET.get('first_name', '')
students = Student.objects.raw(
    "select * from sio_student where first_name = '" + first_name + "'")
response_text = serializers.serialize('json', students)
return HttpResponse(response_text, content_type='application/json')
