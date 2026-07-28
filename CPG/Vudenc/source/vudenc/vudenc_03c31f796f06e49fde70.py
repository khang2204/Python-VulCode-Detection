import praw
import time
from datetime import datetime
from time import sleep
from rpc_bindings import send, open_account, generate_account, generate_qr, nano_to_raw, receive_all, send_all, check_balance, validate_address, open_or_receive
import mysql.connector
import pprint
comment_footer = """


*Nano Tipper Z Bot v0.1. Replies to this comment might be treated as PM commands. This program is in beta testing,
 and your funds could be lost.*
"""
help_text = """
Nano Tipper Z Bot v0.1. Use at your own risk, and don't put in more Nano than you're willing to lose.


To perform a command, create a new message with any of the following commands in the message body.


'create' - Create a new account if one does not exist


'private_key' -  (disabled) Retrieve your account private key


'new_address' - (disabled) If you feel this address was compromised, create a new account and key


'send <amount> <user/address> - Send Nano to a reddit user or an address


'receive' - Receive all pending transactions


'balance' - Retrieve your account balance. Includes both pocketed and unpocketed transactions.


'minimum <amount>' - Sets a minimum amount for receiving tips. Program minimum is 0.001 Nano.


'help' - Get this help message



If you have any questions or bug fixes, please contact /u/zily88.
"""
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('nano_tipper_z+cryptocurrency247')
tip_froms = []
tip_parents = []
tip_tos = []
tip_comments = []
tip_amounts = []
last_action = time.time()
program_minimum = 0.001
recipient_minimum = 0.01
sql_password = f.read()
mydb = mysql.connector.connect(user='root', password=sql_password, host=
    'localhost', auth_plugin='mysql_native_password', database='nano_tipper_z')
mycursor = mydb.cursor()
def stream_comments_messages():...
previous_comments = {comment for comment in subreddit.comments()}
previous_messages = {message for message in reddit.inbox.unread()}
print('received first stream')
while True:
sleep(6)
last_action = time.time()
updated_comments = {comment for comment in subreddit.comments()}
new_comments = updated_comments - previous_comments
previous_comments = updated_comments
updated_messages = {message for message in reddit.inbox.unread()}
new_messages = updated_messages - previous_messages
previous_messages = updated_messages
if len(new_comments) >= 1:
for new_comment in new_comments:
if len(new_messages) >= 1:
print('full name: ', new_comment.name)
for new_message in new_messages:
yield None
if new_comment.name[:3] == 't1_':
print('full name: ', new_message.name)
yield 'comment', new_comment
if new_message.name[:3] == 't4_':
yield 'message', new_message
