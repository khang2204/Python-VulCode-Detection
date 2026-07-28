@data(('9991', 'B0046A36-3F1C-11E9-9A87-005056AA6F01', 0, 0, 0), ('9992',...
email_obj = {'sender': 'Alex Roy <Alex.Roy@dilfo.com>', 'subject':
    f'Re: [EXTERNAL] Upcoming Holdback Release: #{job_number}', 'date':
    'Thu, 30 May 2019 00:41:05 +0000', 'content':
    f"{ground_truth}\r\n\r\nAlex Roy\r\nDilfo Mechanical\r\n(613) 899-9324\r\n\r\n________________________________\r\nFrom: Dilfo HBR Bot <dilfo.hb.release@gmail.com>\r\nSent: Wednesday, May 29, 2019 8:40 PM\r\nTo: Alex Roy\r\nSubject: [EXTERNAL] #{job_number} - Upcoming Holdback Release\r\n\r\nHi Alex,\r\n\r\nYou're receiving this e-mail notification because you added the project #{job_number} - DWS Building Expansion to the watchlist of upcoming holdback releases. \r\n\r\nBefore going any further, please follow the link below to make sure the algorithm correctly matched the project in question:\r\nhttps://link.spamstopshere.net/u/f544cec5/3CEdd3OC6RGV00Hm8I9C_g?u=https%3A%2F%2Fcanada.constructconnect.com%2Fdcn%2Fcertificates-and-notices%2F%2F{dcn_key}\r\n\r\nIf it's the right project, then the certificate was just published this past Wednesday on March 6, 2019. This means a valid holdback release invoice could be submitted as of:\r\nA) April 20, 2019 if the contract was signed before October 1, 2019 or;\r\nB) May 5, 2019 if the contract was signed since then.\r\n\r\nPlease be aware this is a fully automated message. The info presented above could be erroneous.\r\nYou can help improve the matching algorithms by replying to this e-mail with a simple `1` or `0` to confirm whether or not the linked certificate represents the project in question.\r\n\r\nThanks,\r\nDilfo HBR Bot\r\n"
    }
fake_dilfo_insert = """
            INSERT INTO df_dilfo (job_number, closed)
            VALUES ({}, {})
        """
fake_match_insert = """
            INSERT INTO df_matched (job_number, ground_truth)
            VALUES ({}, {})
        """
conn.cursor().execute(fake_dilfo_insert.format(job_number, was_prev_closed))
if was_prev_matched:
if was_prev_closed:
df_dilfo_pre = pd.read_sql(
    f'SELECT * FROM df_dilfo WHERE job_number={job_number}', conn)
conn.cursor().execute(fake_match_insert.format(job_number, 1))
conn.cursor().execute(fake_match_insert.format(job_number, 0))
df_matched_pre = pd.read_sql(
    f'SELECT * FROM df_matched WHERE job_number={job_number}', conn)
process_as_reply(email_obj)
df_dilfo_post = pd.read_sql(
    f'SELECT * FROM df_dilfo WHERE job_number={job_number}', conn)
df_matched_post = pd.read_sql(
    f'SELECT * FROM df_matched WHERE job_number={job_number}', conn)
self.assertEqual(len(df_dilfo_pre), len(df_dilfo_post))
self.assertEqual(df_dilfo_post.iloc[0].closed, was_prev_closed or ground_truth)
self.assertEqual(any(df_matched_post.ground_truth), was_prev_closed or
    ground_truth)
self.assertEqual(len(df_matched_pre) + (not was_prev_closed), len(
    df_matched_post))
self.assertEqual(list(df_matched_pre.columns), list(df_matched_post.columns))
self.assertEqual(list(df_dilfo_pre.columns), list(df_dilfo_post.columns))
