def _create_mail_sender(self):...
mail_sender = Mock()
mail_sender.sendmail.side_effect = lambda mail: succeed(mail)
return mail_sender
