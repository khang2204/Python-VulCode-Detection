@app.route('/json/<newspaper>/<query>')...
hinduscraper = scrapers[newspaper]
hinduscraper.getArticleLinks(query)
hinduscraper.addArticleContent()
articles = hinduscraper.getArticles()
return jsonify(articles=articles)
