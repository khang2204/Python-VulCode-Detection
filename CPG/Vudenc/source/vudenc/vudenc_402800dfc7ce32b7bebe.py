@_transform.route('one_hot_encode_column', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
col = request.form['column']
one_hot_encode(dataset.working_copy, col)
flash('An unexpected error occured while one-hot-encoding the column', 'danger'
    )
flash('Column one-hot-encoded successfully.', 'success')
create_action('One-hot-encoded {0}'.format(col), dataset.id, current_user.id)
return redirect(request.referrer)
