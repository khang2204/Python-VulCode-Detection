def _skw_matches_comparator(kw0, kw1):...
"""docstring"""
list_comparison = cmp(len(kw1[1][0]), len(kw0[1][0]))
if list_comparison:
return list_comparison
if kw0[0].isComposite() and kw1[0].isComposite():
component_avg0 = sum(kw0[1][1]) / len(kw0[1][1])
return cmp(len(str(kw1[0])), len(str(kw0[0])))
component_avg1 = sum(kw1[1][1]) / len(kw1[1][1])
component_comparison = cmp(component_avg1, component_avg0)
if component_comparison:
return component_comparison
