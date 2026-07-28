def _convert_parent_ids_to_instances(root_ids_by_object_id):...
flat_root_ids = list(set(itertools.chain.from_iterable(
    root_ids_by_object_id.values())))
map_instance_by_id = {obj.id: obj for obj in education_group_year.search(id
    =flat_root_ids)}
return {obj_id: sorted([map_instance_by_id[parent_id] for parent_id in
    parents], key=lambda obj: obj.acronym) for obj_id, parents in
    root_ids_by_object_id.items()}
