def discretize_eq_freq(table_name, attr, intervals):...
"""docstring"""
df = pd.read_sql_table(table_name, db.engine)
print('EQUAL FREQUENCY DISCRETIZATION FAILED:\n' + str(e))
attr_length = len(df[attr])
elements_per_interval = attr_length // intervals
sorted_data = list(df[attr].sort_values())
selector = 0
edge_list = []
while selector < attr_length:
if edge_list[-1] != sorted_data[-1] and len(edge_list) == intervals + 1:
edge_list.append(sorted_data[selector])
edge_list[-1] = sorted_data[-1]
if edge_list[-1] != sorted_data[-1] and len(edge_list) != intervals + 1:
selector += elements_per_interval
edge_list[0] = edge_list[0] - edge_list[0] * 0.001
edge_list.append(sorted_data[-1])
edge_list[-1] = edge_list[-1] + edge_list[-1] * 0.001
column_name = attr + '_' + str(intervals) + '_eq_freq_intervals'
discretize_width(table_name, attr, edge_list, df, column_name)
