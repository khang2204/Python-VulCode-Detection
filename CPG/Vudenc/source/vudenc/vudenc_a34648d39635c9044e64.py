import unittest
import pandas as pd
import numpy as np
import datetime
from ddt import ddt, data, unpack
from scraper import scrape
from wrangler import clean_job_number, clean_pub_date, clean_city, clean_company_name, get_acronyms, get_street_number, get_street_name, clean_title, wrangle
from matcher import match
from communicator import communicate
from inbox_scanner import process_as_form, process_as_reply
from ml import build_train_set, train_model, validate_model
from db_tools import create_connection
from test.test_setup import create_test_db
import os
prob_thresh = 0.7
@data((' ', ''), ('\n  #2404\n', '2404'), ('no. 2404', '2404'), ('# 2404',...
output_string = clean_job_number(input_string)
self.assertEqual(desired_string, output_string)
@data((' ', ''), ('\n  2019-02-20\n', '2019-02-20'), ('2019-02-20',...
output_string = clean_pub_date(input_string)
self.assertEqual(desired_string, output_string)
@data((' ', ''), (...
output_string = clean_city(input_string)
self.assertEqual(desired_string, output_string)
@data((' ', ''), ('Frecon', 'frecon'), ('Frecon', 'frecon'), (...
output_string = clean_company_name(input_string)
self.assertEqual(desired_string, output_string)
@data((' ', []), ('Ron Eastern Construction Ltd. (RECL)', ['RECL']), (...
output_string = get_acronyms(input_string)
self.assertEqual(desired_string, output_string)
address_test_data = ('123 Fake St.', '123', 'fake'), ('12 Carrière Rd',
    '12', 'carriere'), ('8-1230 marenger street', '1230', 'marenger'), (
    'apt. 8, 1230 marenger street', '1230', 'marenger'), (
    '8-1230 marenger street, apt. 8, ', '1230', 'marenger'), (
    '1230 apt. 8, marenger street', '1230', 'marenger'), (
    '1010 talbot st. unit #1', '1010', 'talbot'), ('6250 st albans court',
    '6250', 'albans'), ('6250 saint albans court', '6250', 'albans'), (
    '6250 st. albans', '6250', 'albans'), ('6250 st-albans CRT', '6250',
    'albans'), (
    'University of Ottawa, Faculty of Medicine and Faculty of Health Sciences, Roger Guindon Hall, 451 Smyth Road, Ottawa, Ontario K1H 8L1'
    , '451', 'smyth'), ('145 Jean-Jacques Lussier', '145', 'jean-jacques'), (
    'Edwardsburgh/Cardinal', '', '')
@data(*address_test_data)...
output_string = get_street_number(input_string)
self.assertEqual(desired_string1, output_string)
@data(*address_test_data)...
output_string = get_street_name(input_string)
self.assertEqual(desired_string2, output_string)
@data((' ', ''), ('test', 'test'), ('testé', 'teste'))...
output_string = clean_title(input_string)
self.assertEqual(desired_string, output_string)
def setUpClass():...
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
create_test_db()
os.rename(filename, 'temp_' + filename)
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
def tearDownClass():...
os.rename('test_' + filename, filename)
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
@data(('9981', 'B0046A36-3F1C-11E9-9A87-005056AA6F11', 0, 0, 0), ('9982',...
os.rename('temp_' + filename, filename)
os.remove(filename)
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
def setUp(self):...
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
create_test_db()
os.rename(filename, 'temp_' + filename)
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
def tearDown(self):...
os.rename('test_' + filename, filename)
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
def test_scarpe_to_communicate(self):...
os.rename('temp_' + filename, filename)
os.remove(filename)
test_limit = 3
web_df = scrape(limit=test_limit, test=True, since='week_ago')
self.assertEqual(len(web_df), test_limit)
match_first_query = 'SELECT * FROM df_dilfo WHERE closed=0 LIMIT 1'
dilfo_row = pd.read_sql(match_first_query, conn).iloc[0]
communicate(web_df, dilfo_row, test=True)
def test_truth_table(self):...
build_train_set()
train_model(prob_thresh=prob_thresh)
match_query = """
                        SELECT 
                            df_dilfo.job_number,
                            df_dilfo.city,
                            df_dilfo.address,
                            df_dilfo.title,
                            df_dilfo.owner,
                            df_dilfo.contractor,
                            df_dilfo.engineer,
                            df_dilfo.receiver_email,
                            df_dilfo.cc_email,
                            df_dilfo.quality,
                            df_matched.dcn_key,
                            df_matched.ground_truth
                        FROM 
                            df_dilfo 
                        LEFT JOIN 
                            df_matched
                        ON 
                            df_dilfo.job_number=df_matched.job_number
                        WHERE 
                            df_dilfo.closed=1
                        AND
                            df_matched.ground_truth=1
                        AND 
                            df_matched.validate=0
                    """
test_df_dilfo = pd.read_sql(match_query, conn)
test_web_df = scrape(ref=test_df_dilfo)
results = match(df_dilfo=test_df_dilfo, df_web=test_web_df, test=True,
    prob_thresh=prob_thresh, version='new')
qty_actual_matches = int(len(results) ** 0.5)
qty_found_matches = results[results.pred_match == 1].title.nunique()
self.assertTrue(qty_found_matches == qty_actual_matches, msg=
    f'qty_found_matches({qty_found_matches}) not equal qty_actual_matches({qty_actual_matches})'
    )
false_positives = len(results[results.pred_match == 1]) - qty_found_matches
self.assertTrue(false_positives <= round(qty_actual_matches * 0.25, 1), msg
    =
    f'found too many false positives ({false_positives}) out of total test projects ({qty_actual_matches})'
    )
sample_dilfo = pd.DataFrame({'job_number': '2387', 'city': 'Ottawa',
    'address': '2562 Del Zotto Ave., Ottawa, Ontario', 'title':
    'DWS Building Expansion', 'owner': 'Douglas Stalker', 'contractor':
    'GNC', 'engineer': 'Goodkey', 'receiver_email': 'alex.roy@dilfo.com',
    'cc_email': '', 'quality': '2', 'closed': '0'}, index=range(1))
sample_web = pd.DataFrame({'pub_date': '2019-03-06', 'city':
    'Ottawa-Carleton', 'address':
    '2562 Del Zotto Avenue, Gloucester, Ontario', 'title':
    'Construct a 1 storey storage addition to a 2 storey office/industrial building'
    , 'owner': 'Doug Stalker, DWS Roofing', 'contractor':
    'GNC Constructors Inc.', 'engineer': None, 'dcn_key':
    'B0046A36-3F1C-11E9-9A87-005056AA6F02'}, index=range(1))
is_match, prob = match(df_dilfo=sample_dilfo, df_web=sample_web, test=True,
    version='new').iloc[0][['pred_match', 'pred_prob']]
self.assertTrue(is_match, msg=
    f'Project #{sample_dilfo.job_number} did not match successfully. Match probability returned was {prob}.'
    )
results = match(df_dilfo=sample_dilfo, since='2019-03-05', until=
    '2019-03-07', test=True, version='new')
prob_from_db_cert = results[results.contractor == 'gnc'].iloc[0].pred_prob
self.assertTrue(round(prob, 2) == round(prob_from_db_cert, 2))
validate_model(prob_thresh=prob_thresh, test=True)
if __name__ == '__main__':
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
unittest.main(verbosity=2)
os.rename('temp_' + filename, filename)
