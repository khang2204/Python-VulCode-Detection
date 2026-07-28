def __init__(self, field_mapping, paths, custom_methods):...
"""docstring"""
self.base_table = ''
self.field_mapping = self._parse_field_mapping(field_mapping)
self.path_mapping = self._parse_multi_path_mapping(paths)
self.custom_methods = self._parse_custom_methods(custom_methods)
self.WHERE_CONDITION_MAPPING = {self.WHERE_CONDITION:
    '_generate_where_phrase', self.AND_CONDITION: '_parse_and', self.
    OR_CONDITION: '_parse_or', self.NOT_CONDITION: '_parse_not', self.
    EXISTS_CONDITION: '_parse_exists', self.CUSTOM_METHOD_CONDITION:
    '_parse_custom_method_condition'}
