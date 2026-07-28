@application.route('/analogy')...
like1 = request.args.get('like1', '')
like2 = request.args.get('like2', '')
likes = [word.lower() for word in [like1, like2] if word != '']
unlike = request.args.get('unlike', '')
unlike = [word.lower() for word in list(unlike) if word not in ('', '#')]
if not likes and not unlike:
return render_template('analogy.html', analogies=[], error=False)
analogies = model.most_similar(positive=likes, negative=unlike)
return render_template('analogy.html', analogies=[], error=True)
return render_template('analogy.html', analogies=analogies)
