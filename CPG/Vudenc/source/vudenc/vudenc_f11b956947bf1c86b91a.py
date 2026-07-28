def _get_sort_parameters(self):...
"""docstring"""
sort_by = self.model.columns[self.table_view.horizontalHeader().
    sortIndicatorSection()]
sort_asc = self.table_view.horizontalHeader().sortIndicatorOrder()
return sort_by, sort_asc
