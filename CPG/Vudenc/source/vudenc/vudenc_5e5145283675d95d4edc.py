def test_should_create_a_playlist():...
populate_test_database()
response = test_app.post('/playlists/nn')
assert response.json['status'] == 'OK'
response2 = test_app.get('/playlists')
assert response2.json['status'] == 'OK'
assert response2.json['data'] == [dict(id=1, name='nn')]
