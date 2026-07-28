@app.route('/<page_name>/save', methods=['POST'])...
content = request.form.get('content')
query = db.query(
    "select page_content.content, page.id as page_id, page_content.id as content_id from page, page_content where page.id = page_content.page_id and page.page_name = '%s' order by page_content.id desc limit 1"
     % page_name)
result = query.namedresult()
if len(result) < 1:
db.insert('page', {'page_name': page_name})
query = db.query("select id from page where page_name = '%s'" % page_name)
page_id = query.namedresult()[0].id
db.insert('page_content', {'page_id': page_id, 'content': content,
    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', localtime())})
return redirect('/%s' % page_name)
