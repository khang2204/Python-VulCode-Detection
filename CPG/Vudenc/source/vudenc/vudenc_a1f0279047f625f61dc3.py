@app.route('/json/politicians/<politician>')...
politicians = Politician.all()
politicians.filter('name =', politician.lower())
politician = None
for p in politicians:
politician = p
return jsonify(name=politician.name, state=politician.state, party=
    politician.party, constituency=politician.constituency, wiki=politician
    .wiki_link, imageUrl=politician.image_url, search_count=politician.
    search_count)
