def combine_odds(odds, target_types):...
"""docstring"""
combined_odds = 1 / pd.concat([(1 / odds[target_type]) for target_type in
    target_types], axis=1).sum(axis=1)
combined_odds.name = '+'.join(target_types)
return pd.concat([odds, combined_odds], axis=1)
