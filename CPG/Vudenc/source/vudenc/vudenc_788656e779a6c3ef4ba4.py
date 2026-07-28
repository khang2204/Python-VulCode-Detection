@app.route('/run/form/history', methods=['POST'])...
history = json.loads(request.data)
history = [{'id': item['id'], 'date': datetime.fromtimestamp(item['date'] /
    1000), 'commands': item['commands']} for item in history]
return render_template('run_history.html', history=history)
