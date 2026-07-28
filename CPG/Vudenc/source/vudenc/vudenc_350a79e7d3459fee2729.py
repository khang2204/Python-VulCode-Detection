@defer.inlineCallbacks...
mail_ids = yield self.mail_store.get_mailbox_mail_ids(mbox_name)
mails = yield self.mail_store.get_mails(mail_ids)
defer.returnValue(mails)
