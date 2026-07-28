def get_days_distribution(data, groups=None):...
dist = pd.cut(data.groupby('matched_id').days.sum(), [0, 1, 2, 10, 90, 1000
    ], right=False).value_counts(sort=False)
dist = pd.DataFrame({'days': dist.as_matrix()}, index=days_interval_to_text
    (dist.index))
return dist, []
