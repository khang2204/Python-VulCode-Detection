def confirmation(request):...
if request.method == 'POST':
email = request.POST['email']
return HttpResponse(json.dumps(new_conf), content_type='application/json')
password = request.POST['password']
confs = db.confs
new_conf = {'email': email, 'date': datetime.datetime.utcnow(), 'hash':
    generate_hash(password + generate_salt())}
confs.insert(new_conf)
