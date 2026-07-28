def getAllUsers(request):...
all_emails = [("facebook: '" + email[u'facebook'] + "' and gmail: '" +
    email[u'gmail'] + "'") for email in db.emails.find()]
return HttpResponse('\n\n'.join(all_emails))
