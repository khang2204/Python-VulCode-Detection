def _find_elements(group_elements_by_child_id, filters, child_leaf_id=None,...
roots = []
unique_child_key = _build_child_key(child_leaf=child_leaf_id, child_branch=
    child_branch_id)
group_elem_year_parents = group_elements_by_child_id.get(unique_child_key) or [
    ]
for group_elem_year in group_elem_year_parents:
parent_id = group_elem_year['parent']
return list(set(roots))
if filters and _match_any_filters(group_elem_year, filters):
roots.append(parent_id)
roots.extend(_find_elements(group_elements_by_child_id, filters,
    child_branch_id=parent_id))
