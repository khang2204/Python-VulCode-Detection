@app.route('/delete_video/<filename>')...
if 'username' in session:
print(session['username'], file=sys.stdout)
return 'test'
data = users.query.filter_by(Username=session['username']).first()
video = Video.query.filter_by(UserID=data.UserID, Name=filename).first()
if video != None:
os.remove('static/videos/{}'.format(filename))
return "Don't delete other people's videos!"
db.session.delete(video)
db.session.commit()
return redirect(url_for('upload'))
