def __init__(self, object_list, query_params=None, list_display=None,...
self.object_list = object_list
self.model = object_list.model
self.query_params = query_params or {}
self.list_display = list_display or []
self.list_filter = list_filter or []
self.list_search = list_search or []
self.search_query_value = self.query_params.get(search_query_param, '')
self.search_query_param = search_query_param
self.ordering_query_value = self.query_params.get(ordering_query_param, '')
self.ordering_query_param = ordering_query_param
self.columns = self.get_columns()
self.filters = [SmartFilter(self.model, field, self.query_params, self.
    object_list) for i, field in enumerate(self.list_filter, start=1)
    ] if self.list_filter else []
