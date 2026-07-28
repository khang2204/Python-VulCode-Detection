@_transform.route('/discretize_column', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
column = request.form['column']
intervals = request.form['intervals']
if intervals == 'equal-distance':
flash('Invalid list of edges provided.', 'danger')
flash('Column discretized successfully.', 'success')
amount = request.form['amount-dist']
if intervals == 'equal-frequency':
flash('An unexpected error occured while discretizing the column', 'danger')
return redirect(request.referrer)
discretize_width(dataset.working_copy, column, int(amount))
amount = request.form['amount-freq']
edges = str(request.form['custom-edges'])
discretize_eq_freq(dataset.working_copy, column, int(amount))
edges = edges.replace(' ', '')
edge_list = edges.split(',')
if len(edge_list) < 2:
for i in range(len(edge_list)):
edge_list[i] = float(edge_list[i])
discretize_width(dataset.working_copy, column, edge_list)
