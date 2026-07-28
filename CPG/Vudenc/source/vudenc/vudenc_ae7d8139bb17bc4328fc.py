def fetch_all_group_elements_in_tree(root: EducationGroupYear, queryset...
if queryset.model != GroupElementYear:
elements = _fetch_row_sql([root.id])
distinct_group_elem_ids = {elem['id'] for elem in elements}
queryset = queryset.filter(pk__in=distinct_group_elem_ids)
group_elems_by_parent_id = {}
for group_elem_year in queryset:
parent_id = group_elem_year.parent_id
return group_elems_by_parent_id
group_elems_by_parent_id.setdefault(parent_id, []).append(group_elem_year)
