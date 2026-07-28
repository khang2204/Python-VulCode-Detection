def topn(self, column):...
count = 'last_switched'
q = (
    """
        SELECT {0}, count({1}) AS c FROM goflow_records {2} GROUP BY {0} ORDER BY c DESC
        """
    .format(self.columns[column].select(), count, self.build_filter_string()))
return self.query_boilerplate(q)
