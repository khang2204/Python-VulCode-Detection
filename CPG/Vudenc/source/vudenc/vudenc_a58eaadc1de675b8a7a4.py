def __init__(self, query_params, column_id, ordering_query_param):...
self.query_params = query_params
self.column_id = column_id
self.ordering_query_param = ordering_query_param
self.query_order = query_params.get(ordering_query_param)
self.current_columns = [int(col) for col in self.query_order.replace('-',
    '').split('.')] if self.query_order else []
self.current_columns_length = len(self.current_columns)
