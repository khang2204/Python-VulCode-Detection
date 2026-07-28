@_transform.route('normalize_column', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
col = request.form['column']
normalize_attribute(dataset.working_copy, col)
flash('An unexpected error occured while normalizing the column', 'danger')
flash('Column normalized successfully.', 'success')
create_action('Normalized {0}'.format(col), dataset.id, current_user.id)
return redirect(request.referrer)
