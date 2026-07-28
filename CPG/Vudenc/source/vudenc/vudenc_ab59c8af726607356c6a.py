def _sort_kw_matches(skw_matches, limit=0):...
"""docstring"""
sorted_keywords = list(skw_matches.items())
sorted_keywords.sort(_skw_matches_comparator)
return limit and sorted_keywords[:limit] or sorted_keywords
