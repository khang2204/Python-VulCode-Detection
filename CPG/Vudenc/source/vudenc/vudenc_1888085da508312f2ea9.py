def get_or_create_group_element_year(parent, child_branch=None, child_leaf=None...
if child_branch:
return GroupElementYear.objects.get_or_create(parent=parent, child_branch=
    child_branch)
if child_leaf:
return GroupElementYear.objects.get_or_create(parent=parent, child_leaf=
    child_leaf)
return AttributeError('child branch OR child leaf params must be set')
