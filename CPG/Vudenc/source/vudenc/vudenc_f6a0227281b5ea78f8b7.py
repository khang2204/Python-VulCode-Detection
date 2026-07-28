@app.route('/', methods=['GET'])...
"""docstring"""
if request.method == 'GET':
cache_id = uuid4()
return render_template('index.html', cache_id=cache_id)
