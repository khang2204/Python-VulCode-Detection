@app.route('/interact', methods=['POST'])...
msg = request.form['message'].replace('img', 'uwu').replace('location', 'owo'
    ).replace('script', 'uwu')
responses = ['send help', 'what is my purpose',
    'donate to us via bitcoin at: {{ bitcoin_address }}',
    'donate to us via paypal at: {{ paypal_address }}',
    'donate to us via venmo at: {{ venmo_address }}',
    'donate to us via beemit at: {{ beemit_address }}']
return render_template('chatbot.html', msg=msg, resp=random.choice(responses))
