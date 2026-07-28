@app.route('/peti/')...
BODY_CONTENT = ''
curs.execute('select * from PETITION_DATA_TB')
result = curs.fetchall()
BODY_CONTENT += (
    '<h1>새로운 청원들</h1><table class="table table-hover"><thead><tr><th scope="col">N</th><th scope="col">Column heading</th></tr></thead><tbody>'
    )
for i in range(len(result)):
BODY_CONTENT += (
    '<tr><th scope="row">{}</th><td><a href="/peti/a/{}">{}</a></td></tr>'.
    format(result[i][0], result[i][0], result[i][1]))
BODY_CONTENT += '</tbody></table>'
BODY_CONTENT += (
    '<button onclick="window.location.href=\'write\'" class="btn btn-primary" value="publish">청원 등록</button>'
    )
return render_template('index.html', OFORM_APPNAME=LocalSettings.
    OFORM_APPNAME, OFORM_CONTENT=BODY_CONTENT)
