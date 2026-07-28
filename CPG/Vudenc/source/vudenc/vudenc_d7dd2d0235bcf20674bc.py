@app.route('/articles/write/', methods=['GET', 'POST'])...
BODY_CONTENT = ''
if request.method == 'POST':
form_display_name = request.form['form_display_name']
BODY_CONTENT += CONVERSTATIONS_DICT['articles_write']
form_notice_level = request.form['form_notice_level']
return render_template('index.html', OFORM_APPNAME=LocalSettings.
    OFORM_APPNAME, OFORM_CONTENT=BODY_CONTENT)
form_body_content = request.form['form_body_content']
if request.form['submit'] == 'publish':
form_enabled = 1
if request.form['submit'] == 'preview':
form_publish_date = datetime.today()
form_enabled = 0
curs.execute(
    'insert into FORM_DATA_TB (form_display_name, form_notice_level, form_publish_date, form_enabled, form_body_content) values("{}", "{}", "{}", {}, "{}")'
    .format(form_display_name, form_notice_level, form_publish_date,
    form_enabled, form_body_content))
