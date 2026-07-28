@application.route('/')...
if subject is None:
return render_template('browse.html', subjects=get_subjects())
articles = get_articles_by_subject(subject)
return render_template('articles.html', articles=articles, subject=subject)
