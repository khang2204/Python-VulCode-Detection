def test_should_return_a_not_ok_status_when_either_specifying_an_out_of_bounds_or_similar_position(...
populate_test_database()
create_video(1, 'title', 'thumbnail', 1)
create_video(1, 'title2', 'thumbnail2', 2)
response = test_app.put('/videos/1/1/2')
assert response.json['status'] == 'NOK'
assert response.json['message'] != None
response2 = test_app.put('/videos/1/1/5')
assert response2.json['status'] == 'NOK'
assert response2.json['message'] != None
