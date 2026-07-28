@_transform.route('/delete_column', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
col = request.form['column']
delete_attribute(dataset.working_copy, col)
flash('An unexpected error occured while deleting the column', 'danger')
flash('Column deleted successfully.', 'success')
create_action('Deleted column {0}'.format(col), dataset.id, current_user.id)
return redirect(request.referrer)
