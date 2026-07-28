@app.route('/edit_comment/<pic_name>', methods=['POST', 'GET'])...
edit_value = request.form['edit_comment']
return render_template('edit_page.html', edit_value=edit_value, pic_name=
    pic_name)
