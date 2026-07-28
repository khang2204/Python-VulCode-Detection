def _parse_field_mapping(self, field_mapping):...
"""docstring"""
return {field[0]: {self.FIELD_NAME: field[1], self.TABLE_NAME: field[2],
    self.DATA_TYPE: field[3]} for field in field_mapping}
