def test_should_return_a_not_ok_status_when_deleting_a_video_from_an_unknown_playlist_id(...
populate_test_database()
create_playlist('first playlist')
response = test_app.post('/videos/1/title/thumbnail')
assert response.json['status'] == 'OK'
response = test_app.delete('/videos/1/2')
assert response.json['status'] == 'NOK'
assert response.json['message'] != None
