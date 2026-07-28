@app.route('/', methods=['POST'])...
fname = f.name
f.write(request.form['program'])
f.flush()
return check_output(['./pmlcheck', fname], stderr=STDOUT).decode().replace(
    fname + ':', 'Line ')
return e.output.decode().replace(fname + ':', 'Line '), 400
