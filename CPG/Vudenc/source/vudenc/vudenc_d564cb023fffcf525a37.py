def test_should_update_a_playlist_name():...
populate_test_database()
response = test_app.post('/playlists/nn')
assert response.json['status'] == 'OK'
response2 = test_app.put('/playlists/1/name')
assert response2.json['status'] == 'OK'
response3 = test_app.get('/playlists')
assert response3.json['status'] == 'OK'
assert response3.json['data'] == [dict(id=1, name='name')]
