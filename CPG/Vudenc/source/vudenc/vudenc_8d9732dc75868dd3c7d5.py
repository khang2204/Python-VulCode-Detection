@defer.inlineCallbacks...
mails = []
yield self.mail_store.add_mailbox(mailbox)
for _ in range(num):
builder = MailBuilder().with_status(flags).with_tags(tags).with_to(to).with_cc(
    cc).with_bcc(bcc)
defer.returnValue(mails)
builder.with_body(str(random.random()))
input_mail = builder.build_input_mail()
mail = yield self.mail_store.add_mail(mailbox, input_mail.raw)
if tags:
mail.tags |= set(tags)
if flags:
for flag in flags:
if tags or flags:
mail.flags.add(flag)
yield self.mail_store.update_mail(mail)
mails.append(mail)
