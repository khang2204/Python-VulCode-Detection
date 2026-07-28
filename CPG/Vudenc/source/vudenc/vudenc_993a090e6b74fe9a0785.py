def post(self, dataset, email):...
dataset = db.get_dataset(dataset)
user = db.User.select().where(db.User.email == email).get()
da = db.DatasetAccess.select().where(db.DatasetAccess.user == user, db.
    DatasetAccess.dataset == dataset).get()
da.has_access = True
da.save()
db.UserAccessLog.create(user=user, dataset=dataset, action='access_granted')
msg = MIMEMultipart()
msg['to'] = email
msg['from'] = settings.from_address
msg['subject'] = 'Swefreq access granted to {}'.format(dataset.short_name)
msg.add_header('reply-to', settings.reply_to_address)
body = (
    """You now have access to the {} dataset

Please visit https://swefreq.nbis.se/dataset/{}/download to download files.
        """
    .format(dataset.full_name, dataset.short_name, dataset.study.contact_name))
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP(settings.mail_server)
server.sendmail(msg['from'], [msg['to']], msg.as_string())
