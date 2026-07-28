@defer.inlineCallbacks...
mails = yield context.client.mail_store.all_mails()
for mail in mails:
yield context.client.mail_store.delete_mail(mail.ident)
