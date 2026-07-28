@_transform.route('/reset', methods=['GET'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
restore_original(dataset.working_copy)
create_action('restored dataset to original state', dataset.id, current_user.id
    )
return redirect(request.referrer)
