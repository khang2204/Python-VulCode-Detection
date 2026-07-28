def ajax(request):...
def parse_int(s):...
return int(s)
return 0
if request.method == 'POST':
points = parse_int(request.POST.get('points'))
return render(request, 'exercises/ajax_exercise.html', {'url': request.
    build_absolute_uri('{}?{}'.format(reverse('ajax'), request.META.get(
    'QUERY_STRING', '')))})
max_points = parse_int(request.POST.get('max_points'))
url = request.GET.get('submission_url')
def respond_text(text):...
response = HttpResponse(text)
response['Access-Control-Allow-Origin'] = '*'
return response
