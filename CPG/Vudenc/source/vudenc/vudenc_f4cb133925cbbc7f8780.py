def test_should_return_a_not_ok_status_when_updating_an_unknown_playlist_id():...
populate_test_database()
create_playlist('first playlist')
response = test_app.put('/playlists/2/name')
assert response.json['status'] == 'NOK'
assert response.json['message'] != None
