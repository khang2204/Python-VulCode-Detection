def get_metrics(base_path, variable, model, scenario, decade, mask,...
"""docstring"""
decade_begin, decade_end = decade
modeled_files = glob.glob(os.path.join(base_path, model, scenario, variable,
    '*.tif'))
modeled_files = sort_files(only_years(modeled_files, begin=decade_begin,
    end=decade_end, split_on='_', elem_year=-1))
month_grouped = pd.Series(modeled_files).groupby([os.path.basename(i).split
    ('_')[-2] for i in modeled_files])
month_grouped = {i: j.tolist() for i, j in month_grouped}
month_dict = {}
for month in month_grouped:
modeled = month_grouped[month]
return {'_'.join([model, scenario, variable, domain_name, str(decade_begin),
    str(decade_end)]): month_dict}
baseline = [fn.replace(model, '5ModelAvg') for fn in modeled]
args = zip(baseline, modeled)
pool = mp.Pool(ncpus)
arr = np.array(pool.map(wrap_diff, args))
pool.close()
pool.join()
pool.terminate()
pool = None
mean_arr = np.mean(arr, axis=0)
arr = None
masked = np.ma.masked_array(mean_arr, mask == 0)
month_dict[str(month)] = {'stdev': str(np.std(masked)), 'mean': str(np.mean
    (masked)), 'min': str(np.min(masked)), 'max': str(np.max(masked))}
if domain_name == None:
domain_name, = str(np.unique(mask > 0))
