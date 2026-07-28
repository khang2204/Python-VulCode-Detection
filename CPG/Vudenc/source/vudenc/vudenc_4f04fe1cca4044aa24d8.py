@endpoints.route('/')...
if db == None:
init()
tag = request.args.get('tag', default='christmasmike')
data = get_web(db=db)
return render_template('libraries/html/web.html', data=data, tag=tag)
