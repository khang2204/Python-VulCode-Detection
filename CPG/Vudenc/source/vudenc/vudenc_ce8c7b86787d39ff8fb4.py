def test_should_return_a_not_ok_status_when_deleting_a_video_not_from_a_given_playlist(...
populate_test_database()
create_playlist('first playlist')
response = test_app.post('/videos/1/title/thumbnail')
assert response.json['status'] == 'OK'
response = test_app.delete('/videos/2/1')
assert response.json['status'] == 'NOK'
assert response.json['message'] != None
