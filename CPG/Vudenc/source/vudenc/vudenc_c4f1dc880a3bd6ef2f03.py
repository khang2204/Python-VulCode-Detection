@data(('9981', 'B0046A36-3F1C-11E9-9A87-005056AA6F11', 0, 0, 0), ('9982',...
email_obj = {'sender': 'Alex Roy <Alex.Roy@dilfo.com>', 'subject':
    'DO NOT MODIFY MESSAGE BELOW - JUST HIT `SEND`', 'date':
    'Tue, 7 May 2019 17:34:17 +0000', 'content':
    f'job_number={job_number}&title=TEST_ENTRY&city=Ottawa&address=2562+Del+Zotto+Ave.%2C+Ottawa%2C+Ontario&contractor=GCN&engineer=Goodkey&owner=Douglas+Stalker&quality=2&cc_email=&link_to_cert={dcn_key}\r\n'
    }
fake_dilfo_insert = """
            INSERT INTO df_dilfo (job_number, receiver_email, closed)
            VALUES ({}, 'alex.roy616@gmail.com', {})
        """
fake_match_insert = """
            INSERT INTO df_matched (job_number, verifier, ground_truth)
            VALUES ({}, 'alex.roy616@gmail.com', {})
        """
if was_prev_closed or was_prev_tracked:
conn.cursor().execute(fake_dilfo_insert.format(job_number, was_prev_closed))
if was_prev_matched:
if was_prev_closed:
df_dilfo_pre = pd.read_sql(
    f'SELECT * FROM df_dilfo WHERE job_number={job_number}', conn)
conn.cursor().execute(fake_match_insert.format(job_number, 1))
conn.cursor().execute(fake_match_insert.format(job_number, 0))
df_matched_pre = pd.read_sql(
    f'SELECT * FROM df_matched WHERE job_number={job_number}', conn)
process_as_form(email_obj)
df_dilfo_post = pd.read_sql(
    f'SELECT * FROM df_dilfo WHERE job_number={job_number}', conn)
df_matched_post = pd.read_sql(
    f'SELECT * FROM df_matched WHERE job_number={job_number}', conn)
self.assertEqual(len(df_dilfo_post), 1)
self.assertEqual(bool(df_dilfo_post.iloc[0].closed), bool(was_prev_closed or
    dcn_key))
self.assertEqual(any(df_matched_post.ground_truth), bool(was_prev_closed or
    dcn_key))
self.assertEqual(len(df_matched_pre) + bool(dcn_key and not was_prev_closed
    ), len(df_matched_post))
self.assertEqual(list(df_matched_pre.columns), list(df_matched_post.columns))
self.assertEqual(list(df_dilfo_pre.columns), list(df_dilfo_post.columns))
