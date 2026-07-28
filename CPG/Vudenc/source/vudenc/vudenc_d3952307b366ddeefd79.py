def expand_url(request):...
url = request.GET.get('url', None)
exurl = expand(url)
while exurl != url:
url = exurl
return JsonResponse({'url': exurl})
exurl = expand(url)
