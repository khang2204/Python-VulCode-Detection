@_transform.route('/delete_predicate', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
table = table_name_to_object(dataset.working_copy)
condition = ''
columns = []
conditions = []
operators = []
logics = []
for i in request.form:
if i.startswith('column'):
columns.sort()
columns.append(i)
if i.startswith('condition'):
conditions.sort()
conditions.append(i)
if i.startswith('logical'):
logics.sort()
logics.append(i)
if i.startswith('operator'):
operators.sort()
operators.append(i)
for i in range(len(columns)):
if i != len(columns) - 1:
delete_rows(table.name, condition)
flash('condition "{0}" not valid'.format(condition), 'danger')
flash('successfully deleted rows using condition "{0}"'.format(condition),
    'success')
condition += '"' + request.form[columns[i + 1]] + '"'
condition += '"' + request.form[columns[0]] + '"'
create_action('rows deleted with condition "{0}"'.format(condition),
    dataset.id, current_user.id)
return redirect(request.referrer)
if request.form[operators[i + 1]] == 'CONTAINS':
if request.form[operators[0]] == 'CONTAINS':
condition += ' ~ '
if request.form[operators[i + 1]] == 'NOT CONTIANS':
condition += ' ~ '
if request.form[operators[0]] == 'NOT CONTIANS':
condition += "'" + request.form[conditions[i + 1]] + "'"
condition += ' !~ '
condition += request.form[operators[i + 1]]
condition += "'" + request.form[conditions[0]] + "'"
condition += ' !~ '
condition += request.form[operators[0]]
condition += ' ' + request.form[logics[i]] + ' '
