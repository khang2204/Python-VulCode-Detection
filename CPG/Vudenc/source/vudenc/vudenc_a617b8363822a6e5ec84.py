def _get_core_keywords(skw_matches, ckw_matches, spires=False):...
"""docstring"""
output = {}
category = {}
def _get_value_kw(kw):...
"""docstring"""
i = 0
while kw[i].isdigit():
i += 1
if i > 0:
return int(kw[:i])
return 0
