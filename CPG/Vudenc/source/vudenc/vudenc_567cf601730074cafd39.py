def redirect_url():...
home_url = flask.url_for('main.home')
url = flask.request.args.get('next') or flask.request.referrer or home_url
if url == flask.request.url:
return home_url
return url
