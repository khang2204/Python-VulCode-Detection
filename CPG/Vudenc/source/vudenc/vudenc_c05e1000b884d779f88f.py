"""Admin model views for records."""
import json
from flask import flash
from flask_admin.contrib.sqla import ModelView
from flask_babelex import gettext as _
from invenio_admin.filters import FilterConverter
from invenio_db import db
from markupsafe import Markup
from sqlalchemy.exc import SQLAlchemyError
from .api import Record
from .models import RecordMetadata
"""Records admin model view."""
filter_converter = FilterConverter()
can_create = False
can_edit = False
can_delete = True
can_view_details = True
column_list = 'id', 'version_id', 'updated', 'created'
column_details_list = 'id', 'version_id', 'updated', 'created', 'json'
column_labels = dict(id=_('UUID'), version_id=_('Revision'), json=_('JSON'))
column_formatters = dict(version_id=lambda v, c, m, p: m.version_id - 1,
    json=lambda v, c, m, p: Markup('<pre>{0}</pre>'.format(json.dumps(m.
    json, indent=2, sort_keys=True))))
column_filters = 'created', 'updated'
column_default_sort = 'updated', True
page_size = 25
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
