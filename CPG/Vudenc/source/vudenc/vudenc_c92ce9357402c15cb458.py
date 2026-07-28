def delete_model(self, model):...
"""docstring"""
if model.json is None:
if not self.handle_view_exception(e):
return True
return True
record = Record(model.json, model=model)
flash(_('Failed to delete record. %(error)s', error=str(e)), category='error')
db.session.rollback()
record.delete()
return False
db.session.commit()
