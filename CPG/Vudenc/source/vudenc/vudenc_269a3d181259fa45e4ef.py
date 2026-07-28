def sendConf(request):...
confs = db.confs
new_conf = {'email': email, 'hash': hashlib.sha1(email + SALT).hexdigest()}
confs.insert(new_conf)
send_mail('[FreeMail] Email Confirmation', 
    'Confirm your account by clicking on the following link: ' +
    '<a href="localhost:5000/confirm/' + email + '/' + new_conf['hash'] +
    '">Here</a>', 'contact@freemail.com', [email], fail_silently=False)
return HttpResponse('Confirmation page created')
