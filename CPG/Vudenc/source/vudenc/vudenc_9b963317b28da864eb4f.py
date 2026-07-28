def test_should_return_a_not_ok_status_when_deleting_an_unknown_playlist_id():...
populate_test_database()
create_playlist('first playlist')
response = test_app.delete('/playlists/2')
assert response.json['status'] == 'NOK'
assert response.json['message'] != None
