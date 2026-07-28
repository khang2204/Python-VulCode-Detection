def get_queryset(self):...
search = self.request.query_params.get('search', '')
tokens = ' & '.join(search.split())
return Locality.objects.raw(locality_list_search_query.format(tokens=tokens))
