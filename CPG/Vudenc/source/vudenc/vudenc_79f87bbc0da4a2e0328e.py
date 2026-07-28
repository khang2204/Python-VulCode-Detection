def test_admin(app, db):...
"""docstring"""
admin = Admin(app, name='Test')
assert 'model' in record_adminview
assert 'modelview' in record_adminview
model = record_adminview.pop('model')
view = record_adminview.pop('modelview')
admin.add_view(view(model, db.session, **record_adminview))
menu_items = {str(item.name): item for item in admin.menu()}
assert 'Records' in menu_items
assert menu_items['Records'].is_category()
submenu_items = {str(item.name): item for item in menu_items['Records'].
    get_children()}
assert 'Record Metadata' in submenu_items
assert isinstance(submenu_items['Record Metadata'], menu.MenuView)
rec_uuid = str(uuid.uuid4())
Record.create({'title': 'test'}, id_=rec_uuid)
db.session.commit()
index_view_url = url_for('recordmetadata.index_view')
delete_view_url = url_for('recordmetadata.delete_view')
detail_view_url = url_for('recordmetadata.details_view', id=rec_uuid)
res = client.get(index_view_url)
assert res.status_code == 200
db_mock.side_effect = SQLAlchemyError()
res = client.post(delete_view_url, data={'id': rec_uuid}, follow_redirects=True
    )
assert res.status_code == 200
res = client.post(delete_view_url, data={'id': rec_uuid}, follow_redirects=True
    )
assert res.status_code == 200
res = client.get(detail_view_url)
assert res.status_code == 200
assert '<pre>null</pre>' in res.get_data(as_text=True)
res = client.post(delete_view_url, data={'id': rec_uuid}, follow_redirects=True
    )
assert res.status_code == 200
