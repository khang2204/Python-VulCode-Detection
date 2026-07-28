def get_histogram_bar_chart_data(data, distribution_function, shared_ids,...
intersection_data = data[data.matched_id.isin(shared_ids)]
distribution, groups = distribution_function(data)
distribution_intersection, _ = distribution_function(intersection_data, groups)
bins = []
logger.info(data_name)
logger.info(distribution_intersection)
logger.info(len(data.matched_id.unique()))
for bin_index in range(len(distribution)):
return [bins, list(distribution.index)]
of_status = {'x': data_name, 'y': int(distribution.iloc[bin_index]) / len(
    data.matched_id.unique()) * 100}
of_status = {'x': data_name, 'y': 0}
all_status = {'x': 'Jail & Homeless', 'y': int(distribution_intersection.
    iloc[bin_index]) / len(intersection_data.matched_id.unique()) * 100}
all_status = {'x': 'Jail & Homeless', 'y': 0}
bins.append((of_status, all_status))
