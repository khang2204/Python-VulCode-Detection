def test_should_return_all_the_videos_from_a_playlist():...
populate_test_database()
create_playlist('first playlist')
create_video(1, 'the title of the video', 'the url of the video', 1)
create_video(1, 'the title of the video', 'the url of the video', 2)
response = test_app.get('/videos/1')
assert response.json['status'] == 'OK'
assert response.json['data'] == [dict(id=1, title='the title of the video',
    thumbnail='the url of the video', position=1), dict(id=2, title=
    'the title of the video', thumbnail='the url of the video', position=2)]
