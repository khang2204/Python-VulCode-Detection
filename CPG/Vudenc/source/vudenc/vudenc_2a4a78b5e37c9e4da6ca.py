def clean_fields(self, exclude=None):...
super().clean_fields(exclude=exclude)
if self.tracker.has_changed('group_type_id') and self.extracted_docs():
msg = (
    'The Group Type may not be changed once extracted documents have been associated with the group.'
    )
