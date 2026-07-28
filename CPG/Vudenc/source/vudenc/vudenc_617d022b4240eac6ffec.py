@app.route('/tmp', methods=['POST'])...
content = base64.b64decode(request.form['content']).decode()
f.write(content)
session['tempFile'] = f.name
return ''
