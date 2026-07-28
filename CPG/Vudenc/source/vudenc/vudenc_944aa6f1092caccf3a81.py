@endpoints.route('/web')...
if db == None:
init()
return json.dumps(get_web(tag, db=db))
