@_transform.route('/change_type', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
table = table_name_to_object(dataset.working_copy)
col = request.form['column']
col = col[:col.find('(') - 1]
new_type = request.form['type']
if col != '' and new_type != '':
return redirect(request.referrer)
change_attribute_type(table.name, col, new_type)
flash('{0} could not be converted to {1}'.format(col, new_type), 'danger')
flash('{0} successfully  converted to {1}'.format(col, new_type), 'success')
create_action('type {0} changed to {1}'.format(col, new_type), dataset.id,
    current_user.id)
