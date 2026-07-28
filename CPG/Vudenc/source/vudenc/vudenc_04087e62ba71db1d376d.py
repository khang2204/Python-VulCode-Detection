def test_should_return_all_playlists():...
populate_test_database()
create_playlist('first playlist')
create_playlist('second playlist')
response = test_app.get('/playlists')
assert response.json['status'] == 'OK'
assert response.json['data'] == [dict(id=1, name='first playlist'), dict(id
    =2, name='second playlist')]
