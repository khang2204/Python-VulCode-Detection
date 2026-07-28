@app.route('/view/<sid>')...
if '/' not in sid:
path = os.path.join(app.config['UPLOAD_FOLDER'], sid)
abort(403)
if os.path.isdir(path):
using_firebase = 'true' if app.config['FIREBASE'] else 'false'
abort(404)
return render_template('view.html', sid=sid, title='Progress for %s' % sid,
    using_firebase=using_firebase)
