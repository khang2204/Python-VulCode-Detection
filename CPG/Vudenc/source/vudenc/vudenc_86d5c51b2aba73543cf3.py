import praw
import re
from datetime import datetime
import operator
import sqlite3
def getDate(submission):...
time = datetime.fromtimestamp(submission.created)
return time.strftime('%Y-%m-%d %H:%M:%S')
