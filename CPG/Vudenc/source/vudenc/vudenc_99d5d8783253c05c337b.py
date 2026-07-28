def set_mapping_level(self, level: MappingLevel):...
"""docstring"""
self.mapping_level = level.value
db.session.commit()
