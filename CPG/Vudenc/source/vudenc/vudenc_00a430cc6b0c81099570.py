@app.route('/upload', methods=['POST'])...
data = {'secret': app.config['G_CAPTCHA_SECRET'], 'response': request.form[
    'g-recaptcha-response'], 'remoteip': request.remote_addr}
resp = requests.post(app.config['G_CAPTCHA_VERIFY'], data=data).json()
if resp['success']:
form = ProcessingForm()
flash('Error: %s' % ', '.join(resp['error-codes']))
if not form.validate_on_submit():
return redirect(url_for('experiment', title='Try it Out!', sitekey=app.
    config['G_CAPTCHA_SITEKEY'], form=form, files=utils.SAMPLE_FILES))
for field, errors in form.errors.items():
path = tempfile.mkdtemp(dir=app.config['UPLOAD_FOLDER'], prefix='')
for e in errors:
session_id = os.path.basename(path)
flash('Error in %s: %s' % (getattr(form, field).label.text, e))
request.files['testcsv'].save(os.path.join(path, app.config['TESTING_FN']))
if request.files['trainingcsv'].filename != '':
request.files['trainingcsv'].save(os.path.join(path, app.config['TRAINING_FN'])
    )
fn = FILE_MAP[request.form['trainingset']]
flash("Error: '%s' is not supported" % request.form['trainingset'])
link = '<a href="%s" class="alert-link">page</a>' % url_for('view', sid=
    session_id)
copyfile(os.path.join(app.config['TRAINING_FOLDER'], fn), os.path.join(path,
    app.config['TRAINING_FN']))
success_txt = 'Success! To view progress later, bookmark the %s' % link
flash(Markup(success_txt))
f = open(os.path.join(path, 'logs.txt'), 'w')
env = os.environ.copy()
env['API_KEY'] = app.config['API_KEY']
sub.Popen(['python', 'scripts/master.py', session_id, request.form[
    'trainingset']], stdout=f, stderr=f, env=env)
return redirect(url_for('view', sid=session_id))
