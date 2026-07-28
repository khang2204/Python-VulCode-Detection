def _build_parent_list_by_education_group_year_id(academic_year, filters=None):...
columns_needed_for_filters = filters.keys() if filters else []
group_elements = list(search(academic_year=academic_year).filter(
    parent__isnull=False).filter(Q(child_leaf__isnull=False) | Q(
    child_branch__isnull=False)).select_related(
    'education_group_year__education_group_type').values('parent',
    'child_branch', 'child_leaf', *columns_needed_for_filters))
result = {}
for group_element_year in group_elements:
key = _build_child_key(child_branch=group_element_year['child_branch'],
    child_leaf=group_element_year['child_leaf'])
return result
result.setdefault(key, []).append(group_element_year)
