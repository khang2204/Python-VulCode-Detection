@app.route('/demo2', methods=['GET', 'POST'])...
z = demo(1)
results = [[x[0], x[1], x[2]] for x in z]
return render_template('demo2.html', query=query1, rows=results)
