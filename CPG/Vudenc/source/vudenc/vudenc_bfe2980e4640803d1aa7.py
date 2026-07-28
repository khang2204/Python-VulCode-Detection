def test_should_return_a_not_ok_status_when_creating_a_video_from_an_unknown_playlist_id(...
populate_test_database()
create_playlist('first playlist')
response = test_app.post('/videos/2/title/thumbnail')
assert response.json['status'] == 'NOK'
assert response.json['message'] != None
