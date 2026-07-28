@_transform.route('/fill_null', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
column_and_type = request.form['column']
column_name = column_and_type[:column_and_type.find(' ')]
column_type = column_and_type[column_and_type.find('(') + 1:column_and_type
    .rfind(')')]
fill_value = request.form['fill_value']
if fill_value == '~option-average~':
flash('An unexpected error occured while performing the operation', 'danger')
flash('Fill operation completed successfully', 'success')
if column_type not in ['INTEGER', 'BIGINT', 'DOUBLE PRECISION']:
if fill_value == '~option-median~':
return redirect(request.referrer)
flash('Operation not supported for this column type.', 'danger')
fill_null_with_average(dataset.working_copy, column_name)
if column_type not in ['INTEGER', 'BIGINT', 'DOUBLE PRECISION']:
is_text_type = column_type in ['TEXT', 'VARCHAR(10)', 'VARCHAR(25)',
    'VARCHAR(255)']
create_action('Filled null values in {0} with average'.format(column_name),
    dataset.id, current_user.id)
flash('Operation not supported for this column type.', 'danger')
fill_null_with_median(dataset.working_copy, column_name)
fill_null_with(dataset.working_copy, column_name, fill_value, is_text_type)
create_action('Filled null values in {0} with median'.format(column_name),
    dataset.id, current_user.id)
create_action('Filled null values in {0} with {1}'.format(column_name,
    fill_value), dataset.id, current_user.id)
