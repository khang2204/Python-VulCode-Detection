def topn_sum(self, column, sum_by):...
q = (
    """
        SELECT {0}, sum({1}) AS c FROM test_goflow_records {2} GROUP BY {3} ORDER BY c DESC
        """
    .format(self.columns[column].select(), sum_by, self.build_filter_string
    (), self.columns[column].name))
print(q)
return self.query_boilerplate(q)
