def test_should_return_a_playlist():...
populate_test_database()
create_playlist('first playlist')
response = test_app.get('/playlists/1')
assert response.json['status'] == 'OK'
assert response.json['data'] == dict(id=1, name='first playlist',
    video_position=0)
