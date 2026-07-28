@_transform.route('/delete_selection', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
selected_data = request.form.getlist('data_id')
table = table_name_to_object(dataset.working_copy)
for data in selected_data:
table.delete(table.c.index == data).execute()
create_action('deleted selected items', dataset.id, current_user.id)
return redirect(request.referrer)
