@app.route('/peti/write/', methods=['GET', 'POST'])...
BODY_CONTENT = ''
if request.method == 'POST':
form_display_name = request.form['form_display_name']
BODY_CONTENT += open('templates/petitions.html', encoding='utf-8').read()
form_author_name = request.form['form_author_name']
return render_template('index.html', OFORM_APPNAME=LocalSettings.
    OFORM_APPNAME, OFORM_CONTENT=BODY_CONTENT)
form_body_content = request.form['form_body_content']
form_body_content = form_body_content.replace('"', '\\"')
form_enabled = 1
form_author = form_author_name
form_publish_date = datetime.today()
curs.execute(
    'insert into PETITION_DATA_TB (form_display_name, form_publish_date, form_enabled, form_author, form_body_content) values("{}", "{}", {}, "{}", "{}")'
    .format(form_display_name, form_publish_date, form_enabled, form_author,
    form_body_content))
conn.commit()
return redirect('/peti')
