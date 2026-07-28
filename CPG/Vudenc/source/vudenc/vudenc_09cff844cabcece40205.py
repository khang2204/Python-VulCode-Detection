@_transform.route('/rename_column', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
col = request.form['column']
new_name = request.form['new_name']
rename_attribute(dataset.working_copy, col, new_name)
flash('An unexpected error occured while renaming the column', 'danger')
flash('Column renamed successfully.', 'success')
create_action('Renamed column {0} to {1}'.format(col, new_name), dataset.id,
    current_user.id)
return redirect(request.referrer)
