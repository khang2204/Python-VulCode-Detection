def _get_root_filters():...
root_type_names = education_group_type.search(category=
    education_group_categories.MINI_TRAINING).exclude(name=GROUP_TYPE_OPTION
    ).values_list('name', flat=True)
root_categories = [education_group_categories.TRAINING]
return {'parent__education_group_type__name': root_type_names,
    'parent__education_group_type__category': root_categories}
