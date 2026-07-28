@app.route('/search')...
limit = 10
offset = 0
user_term = request.args.get('term')
page = request.args.get('page')
term = user_term
if not page:
page = 1
offset = limit * (int(page) - 1)
transliterate_regex = re.compile('.*[a-zA-Z].*')
if transliterate_regex.match(term):
term = transliterate(term, sanscript.ITRANS, sanscript.DEVANAGARI)
term = term.replace('*', '%')
term_words = term.split()
con.row_factory = sql.Row
con.close()
cur = con.cursor()
if len(term_words) == 1:
cur.execute(
    "select * from pada inner join mula on pada.sloka_line = mula.sloka_line where pada like '%s' or artha like '%s' order by id limit %d offset %d;"
     % (term, term, limit, offset))
query = (
    'select * from pada inner join mula on pada.sloka_line = mula.sloka_line where pada in (%s) order by pada limit 100;'
     % ','.join('?' for i in term_words))
rows = cur.fetchall()
rows = cur.execute(query, term_words)
return render_template('search.html', rows=rows, user_term=user_term, term=
    term, page=page)
