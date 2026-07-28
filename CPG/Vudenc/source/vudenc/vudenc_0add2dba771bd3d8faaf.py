@app.route('/', methods=['GET', 'POST'])...
if request.method == 'POST':
url = request.form['url']
return render_template('home.html')
parsed = urlparse(url)
session['domain'] = parsed.netloc
session['url'] = url
return redirect(url_for('crawling'))
