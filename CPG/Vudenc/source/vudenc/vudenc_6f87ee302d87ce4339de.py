@app.route('/resetCurrent')...
session.pop('currentFile', None)
session.pop('tempFile', None)
return ''
