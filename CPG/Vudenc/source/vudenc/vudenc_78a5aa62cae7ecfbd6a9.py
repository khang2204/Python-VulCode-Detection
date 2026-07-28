@app.route('/', methods=['GET', 'POST'])...
BODY_CONTENT = ''
BODY_CONTENT += open('templates/index_content.html', encoding='utf-8').read()
BODY_CONTENT = BODY_CONTENT.replace('| version |', LocalSettings.OFORM_RELEASE)
curs.execute('select * from FORM_DATA_TB')
form_data = curs.fetchall()
for i in range(len(form_data)):
return render_template('index.html', OFORM_APPNAME=LocalSettings.
    OFORM_APPNAME, OFORM_CONTENT=BODY_CONTENT)
