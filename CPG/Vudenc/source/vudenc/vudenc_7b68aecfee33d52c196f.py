def search(**kwargs):...
queryset = GroupElementYear.objects
if 'academic_year' in kwargs:
academic_year = kwargs['academic_year']
if 'child_leaf' in kwargs:
queryset = queryset.filter(Q(parent__academic_year=academic_year) | Q(
    child_branch__academic_year=academic_year) | Q(
    child_leaf__academic_year=academic_year))
queryset = queryset.filter(child_leaf=kwargs['child_leaf'])
return queryset
