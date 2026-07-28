@app.route('/experiment', methods=['GET'])...
form = ProcessingForm(request.form)
return render_template('experiment/index.html', title='Try it Out!',
    sitekey=app.config['G_CAPTCHA_SITEKEY'], form=form, files=utils.
    SAMPLE_FILES)
