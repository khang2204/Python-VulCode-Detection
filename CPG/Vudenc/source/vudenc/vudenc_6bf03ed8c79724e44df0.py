@application.route('/article/<main_article_id>')...
main_article = get_article(main_article_id)
sims = model.docvecs.most_similar(int(main_article_id), topn=10)
sim_articles = get_articles([int(index) for index, sim in sims])
sort_these = []
for article in sim_articles:
sim_score = [score for idx, score in sims if article['index'] == idx][0]
return render_template('doc.html', main_article=main_article, sims=sort_these)
article.extend([round(sim_score, 2)])
sort_these.append(article)
