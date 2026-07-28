@app.route('/upload', methods=['GET', 'POST'])...
error = ''
if 'username' in session:
return render_template('upload', error=e)
if request.method == 'POST':
if 'file' in request.files.keys():
videos = []
f = request.files['file']
if 'link11' in request.form.keys():
for video in os.listdir('static/videos'):
f.save('static/videos/{}'.format(f.filename))
url = request.form['link11']
video_uploader = Video.query.filter_by(Name=video).first()
return render_template('upload.html', videos=videos)
data = users.query.filter_by(Username=session['username']).first()
filename123 = url.split('/')[-1]
video_uploader = users.query.filter_by(UserID=video_uploader.UserID).first()
new_video = Video(VideoID=None, UserID=data.UserID, URL='local', Name=f.
    filename, UploadDate=datetime.today().strftime('%Y-%m-%d'))
urllib.request.urlretrieve(url, 'static/videos/' + filename123)
videos.append((video, video_uploader.Username))
db.session.add(new_video)
data = users.query.filter_by(Username=session['username']).first()
db.session.commit()
new_video = Video(VideoID=None, UserID=data.UserID, URL='local', Name=
    filename123, UploadDate=datetime.today().strftime('%Y-%m-%d'))
db.session.add(new_video)
db.session.commit()
