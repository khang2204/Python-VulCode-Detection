def file(request):...
if request.method == 'POST':
if 'myfile' in request.FILES and request.FILES['myfile'].name:
return render(request, 'exercises/file_exercise.html')
status = 'accepted'
status = 'error'
return render(request, 'exercises/file_result.html', {'status': status})
