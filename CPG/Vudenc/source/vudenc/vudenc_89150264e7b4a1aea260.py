@app.route('/peti/a/<form_id>/')...
if form_id == '':
return 404
BODY_CONTENT = ''
print(form_id)
curs.execute('select * from PETITION_DATA_TB where form_id = {}'.format(
    form_id))
return 404
form_display_name = result[0][1]
result = curs.fetchall()
form_publish_date = result[0][2]
form_author = result[0][4]
form_body_content = result[0][5]
BODY_CONTENT += open('templates/peti_viewer.html').read()
BODY_CONTENT = BODY_CONTENT.replace(' form_display_name ', form_display_name)
BODY_CONTENT = BODY_CONTENT.replace(' form_publish_date ', form_publish_date)
BODY_CONTENT = BODY_CONTENT.replace(' form_author ', form_author)
BODY_CONTENT = BODY_CONTENT.replace(' form_body_content ', form_body_content)
return render_template('index.html', OFORM_APPNAME=LocalSettings.
    OFORM_APPNAME, OFORM_CONTENT=BODY_CONTENT)
