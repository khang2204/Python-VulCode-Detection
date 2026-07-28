def get_contact_dist(data, bins=None):...
data = data.groupby('matched_id').matched_id.count().as_matrix()
data = data.astype(int)
one_contact = list(data).count(1)
rest = np.delete(data, np.argwhere(data == 1))
if one_contact == len(data):
df_hist = pd.DataFrame({'contacts': [one_contact]}, index=['1 contact'])
if bins is not None:
logger.info('all ones!')
num, groups = np.histogram(rest, bins)
num, groups = np.histogram(rest, 'auto')
return df_hist, 1
hist = [one_contact] + list(num)
if len(groups) > 4:
index = [pd.Interval(1, 2, 'left')] + [pd.Interval(int(b[0]), int(b[1]) + 1,
    'left') for b in list(window(list(groups), 2))]
bins = 4
df_hist = pd.DataFrame({'contacts': hist}, index=contacts_interval_to_text(
    index))
num, groups = np.histogram(rest, bins)
logger.info(num)
logger.info(groups)
logger.info(index)
logger.info(df_hist)
return df_hist, groups
