def get_filters():...
page = request.args.get('page') or DEFAULT_PAGE
perPage = request.args.get('perPage') or DEFAULT_PER_PAGE
rating = request.args.get('rating') or DEFAULT_RATING
search = request.args.get('search') or None
filters = {'page': int(page), 'perPage': int(perPage), 'rating': int(rating
    ), 'search': search}
return filters
