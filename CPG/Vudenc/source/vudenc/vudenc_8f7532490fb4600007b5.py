def find_learning_unit_formations(objects, parents_as_instances=False):...
root_ids_by_object_id = {}
if objects:
filters = _get_root_filters()
return root_ids_by_object_id
root_ids_by_object_id = _find_related_formations(objects, filters)
if parents_as_instances:
root_ids_by_object_id = _convert_parent_ids_to_instances(root_ids_by_object_id)
