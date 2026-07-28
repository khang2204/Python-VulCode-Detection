def _get_singlekws(skw_matches, spires=False):...
"""docstring"""
output = {}
for single_keyword, info in skw_matches:
output[single_keyword.output(spires)] = len(info[0])
return output
