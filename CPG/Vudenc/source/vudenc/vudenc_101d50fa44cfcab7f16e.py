def is_condition(cond_or_list):...
return len(cond_or_list) == 3 and cond_or_list[1
    ] in schemas.CONDITION_OPERATORS and isinstance(cond_or_list[0], (six.
    string_types, tuple, list))
