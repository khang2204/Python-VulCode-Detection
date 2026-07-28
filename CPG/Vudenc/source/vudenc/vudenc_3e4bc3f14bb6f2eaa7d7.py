def test_should_return_a_not_ok_status_when_updating_a_video_from_an_unknown_id(...
populate_test_database()
response = test_app.put('/videos/1/1/2')
assert response.json['status'] == 'NOK'
assert response.json['message'] != None
