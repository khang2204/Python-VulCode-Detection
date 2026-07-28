def process_as_form(email_obj):...
dict_input = {unquote(x.split('=')[0]): str(unquote(x.split('=')[1])).
    replace('+', ' ') for x in email_obj['content'].split('&')}
job_number = dict_input['job_number']
was_prev_closed = pd.read_sql(
    f'SELECT * FROM df_dilfo WHERE job_number={job_number}', conn).iloc[0
    ].closed
was_prev_closed = 0
receiver_email = re.findall('<?(\\S+@\\S+\\.\\w+)>?', email_obj['sender'])[0
    ].lower()
dict_input.update({'receiver_email': receiver_email})
if dict_input['cc_email'] != '':
dcn_key = dict_input.pop('link_to_cert')
dcn_key = ''
if dcn_key:
dict_input['cc_email'] += '@dilfo.com'
dcn_key = dcn_key.split('-notices/')[1]
dcn_key = re.findall('[\\w-]*', dcn_key)[0]
dict_input.pop('instant_scan')
instant_scan = False
if was_prev_closed:
instant_scan = True
logger.info(
    f'job was already matched successfully and logged as `closed`. Sending e-mail!'
    )
if dcn_key:
prev_match = pd.read_sql(
    'SELECT * FROM df_matched WHERE job_number=? AND ground_truth=1', conn,
    params=[job_number]).iloc[0]
dict_input.update({'closed': 1})
dict_input.update({'closed': 0})
verifier = prev_match.verifier
df = pd.read_sql('SELECT * FROM df_matched', conn)
df = pd.read_sql('SELECT * FROM df_dilfo', conn)
log_date = prev_match.log_date
match_dict_input = {'job_number': dict_input['job_number'], 'dcn_key':
    dcn_key, 'ground_truth': 1, 'verifier': dict_input['receiver_email'],
    'source': 'input', 'log_date': str(datetime.datetime.now().date()),
    'validate': 0}
df = df.append(dict_input, ignore_index=True)
dcn_key = prev_match.dcn_key
df = df.append(match_dict_input, ignore_index=True)
for dup_i in df[df.duplicated(subset=['job_number'], keep='last')].index:
message = f"""From: Dilfo HBR Bot
To: {receiver_email}
Subject: Previously Matched: #{job_number}

Hi {receiver_email.split('.')[0].title()},

It looks like job #{job_number} corresponds to the following certificate:
{lookup_url}{dcn_key}

This confirmation was provided by {verifier.split('.')[0].title()}{' on ' + log_date if log_date is not None else ''}.

If any of the information above seems to be inaccurate, please reply to this e-mail for corrective action.

Thanks,
Dilfo HBR Bot
"""
df = df.drop_duplicates(subset=['job_number', 'dcn_key'], keep='last')
dup_job_number = df.iloc[dup_i].job_number
df.to_sql('df_dilfo', conn, if_exists='replace', index=False)
context = ssl.create_default_context()
logger.info('password not available -> could not send e-mail')
return
df.to_sql('df_matched', conn, if_exists='replace', index=False)
dup_receiver = df.iloc[dup_i].receiver_email
if instant_scan:
server.login(sender_email, password)
dup_cc = df.iloc[dup_i].cc_email
dilfo_query = 'SELECT * FROM df_dilfo WHERE job_number=?'
server.sendmail(sender_email, [receiver_email], message)
df = df.drop(dup_i)
df_dilfo = pd.read_sql(dilfo_query, conn, params=[job_number])
logger.info(f'Successfully sent an email to {receiver_email}')
dup_addrs = '; '.join([x for x in dup_cc + dup_receiver if x])
hist_query = 'SELECT * FROM df_hist ORDER BY pub_date DESC LIMIT 2000'
update_i = df[df.job_number == dup_job_number].index
df_web = pd.read_sql(hist_query, conn)
df.loc[update_i, 'cc_email'] = df.loc[update_i, 'cc_email'] + '; ' + dup_addrs
results = match(df_dilfo=df_dilfo, df_web=df_web, test=False)
if len(results[results.pred_match == 1]) == 0:
message = f"""From: Dilfo HBR Bot
To: {receiver_email}
Subject: Successful Project Sign-Up: #{job_number}

Hi {receiver_email.split('.')[0].title()},

Your information for project #{job_number} was logged successfully but no corresponding certificates in recent history were matched to it.

Going forward, the Daily Commercial News website will be scraped on a daily basis in search of your project. You will be notified if a possible match has been detected.

Thanks,
Dilfo HBR Bot
"""
context = ssl.create_default_context()
logger.info('password not available -> could not send e-mail')
server.login(sender_email, password)
server.sendmail(sender_email, [receiver_email], message)
logger.info(f'Successfully sent an email to {receiver_email}')
