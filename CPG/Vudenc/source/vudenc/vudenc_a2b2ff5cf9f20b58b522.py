def first(request):...
if request.method == 'POST':
submission = request.POST.get('answer', '').lower()
return render(request, 'exercises/first_exercise.html')
points = 0
if 'hello' in submission:
points += 1
if 'a+' in submission:
points += 1
return render(request, 'exercises/first_result.html', {'points': points,
    'max_points': 2})
