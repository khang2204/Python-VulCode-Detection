def _find_related_formations(objects, filters):...
_raise_if_incorrect_instance(objects)
academic_year = _extract_common_academic_year(objects)
parents_by_id = _build_parent_list_by_education_group_year_id(academic_year,
    filters=filters)
if isinstance(objects[0], LearningUnitYear):
return {obj.id: _find_elements(parents_by_id, filters, child_leaf_id=obj.id
    ) for obj in objects}
return {obj.id: _find_elements(parents_by_id, filters, child_branch_id=obj.
    id) for obj in objects}
