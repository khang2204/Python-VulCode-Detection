def api(environ, start_response):...
"""docstring"""
if environ['REQUEST_METHOD'] == 'POST':
if environ['REQUEST_METHOD'] == 'DELETE':
post = getFields(environ)
start_response('500 ERROR', [('Content-Type', 'text/json')])
if environ['REQUEST_METHOD'] == 'PUT':
delete = getFields(environ)
start_response('500 ERROR', [('Content-Type', 'text/json')])
db = mysql.MySQL()
return [str.encode(json.dumps({'success': 'false', 'error': 500, 'method':
    'POST', 'msg': 'Não foi possível adicionar contato'}))]
if environ['REQUEST_METHOD'] == 'GET':
put = getFields(environ)
start_response('500 ERROR', [('Content-Type', 'text/json')])
db = mysql.MySQL()
return [str.encode(json.dumps({'success': 'false', 'error': 500, 'method':
    'DELETE', 'msg': 'Não foi possível deletar contato'}))]
db.insert('users', {'nome': post['nome'].value, 'sobrenome': post[
    'sobrenome'].value, 'endereco': post['endereco'].value})
db = mysql.MySQL()
start_response('500 ERROR', [('Content-Type', 'text/json')])
db = mysql.MySQL()
return [str.encode(json.dumps({'success': 'false', 'error': 500, 'method':
    'PUT', 'msg': 'Não foi possível atualizar contato'}))]
db.delete_where('users', 'id = {}'.format(delete['id'].value))
start_response('200 OK', [('Content-Type', 'text/json')])
json_data = db.select('users')
return [str.encode(json.dumps({'success': 'false', 'error': 500, 'method':
    'GET', 'msg': 'Não foi possível retornar tabela'}))]
db.update_where('users', "nome = '" + put['nome'].value +
    "', sobrenome = '" + put['sobrenome'].value + "', endereco = '" + put[
    'endereco'].value + "'", 'id = ' + put['id'].value)
start_response('200 OK', [('Content-Type', 'text/json')])
return [str.encode(json.dumps({'success': 'true'}))]
html = str.encode(json.dumps(json_data))
start_response('200 OK', [('Content-Type', 'text/json')])
return [str.encode(json.dumps({'success': 'true'}))]
start_response('200 OK', [('Content-Type', 'text/json')])
return [str.encode(json.dumps({'success': 'true'}))]
return [html]
