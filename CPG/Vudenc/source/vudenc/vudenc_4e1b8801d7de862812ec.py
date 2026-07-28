def send_message(message):...
"""docstring"""
if not recipients:
logging.warn('no recipients set, not sending any message')
send_mail(sender=smtp_sender, tolist=recipients, subject=
    'SolrCheckup Warnung!', message=message, smtp=smtp_server, smtp_port=
    smtp_port, username=smtp_name, password=smtp_password)
return
