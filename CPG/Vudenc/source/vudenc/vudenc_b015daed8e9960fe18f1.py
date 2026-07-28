def generate_date_mapping(date_value, tags, path_string):...
"""docstring"""
time_string = date_value.strftime(path_string)
path_string = tpl(time_string, **tags.__dict__)
return path_string
