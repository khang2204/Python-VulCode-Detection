def flows(self):...
c = []
for col in self.column_order:
c.append(self.columns[col].select())
q = (
    """
        SELECT {1} FROM goflow_records {0} ORDER BY last_switched DESC
        """
    .format(self.build_filter_string(), ', '.join(c)))
print(q)
return self.query_boilerplate(q)
