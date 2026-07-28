@login_required...
term = request.GET['term']
results = _get_previously_used(Keyword, term)
results.extend(_get_fast_results(term))
return JsonResponse({'err': 'nil', 'results': results})
