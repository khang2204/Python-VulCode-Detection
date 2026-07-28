@application.route('/search', methods=['POST'])...
if request.method == 'POST':
query = request.form['search']
q_vec = model.infer_vector(query.split())
results = model.docvecs.most_similar(positive=[q_vec], topn=100)
results = [int(r[0]) for r in results]
results = get_articles(results)
return render_template('search.html', articles=results)
