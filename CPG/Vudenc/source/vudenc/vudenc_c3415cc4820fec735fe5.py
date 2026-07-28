@app.route('/results')...
results = load_json('results.json')
time_series = []
for name, values in results.items():
ts = {'id': name, 'values': {'x': [], 'y': []}}
time_series.sort(key=lambda ts_item: ts_item['result_type'], reverse=False)
dates = [key for key in values]
return render_template('results.html', results=results, time_series=time_series
    )
dates.sort()
for date in dates:
ts['values']['x'].append(date)
if re.search(':timeseries$', name):
ts['values']['y'].append(values[date])
attrs = name.split(':')
if re.search('\\(output,.*\\)$', name):
(ts_name, ts_author), rest = attrs[:2], attrs[2:]
name_wo_braces = re.sub('[()]', '', name)
if re.search('input,source_type:', name):
ts['result_type'] = 'Input time series'
attrs = name_wo_braces.split(',')
attrs = name.split(',')
time_series.append(ts)
ts['ts_name'] = ts_name
(ts_name, ts_author, _, model_name), rest = attrs[:4], attrs[4:]
(ts_name, model_name, ts_author, _), source = attrs[:4], attrs[4:]
ts['ts_author'] = ts_author
ts['result_type'] = 'Output time series'
ts['result_type'] = 'Intermediate input time series'
ts['ts_name'] = ts_name
ts['ts_name'] = ts_name
ts['ts_author'] = ts_author
ts['ts_author'] = ts_author
ts['model_name'] = model_name
ts['model_name'] = model_name
if re.search('input,source_type:output', name):
source_model_name, rest = source[1], source[2:]
ts['source_type'] = 'timeseries'
ts['source_model_name'] = source_model_name
ts['source_type'] = 'model'
