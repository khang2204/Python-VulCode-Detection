import cmd
import getpass
import paramiko
from shrub.scripts.validate import validate
CONNECTION_STRING = 'shrub@104.236.0.123'
SERVER_PASSWORD = 'swordfish'
prompt = 'shrub> '
intro = """Welcome to shrub!
To get started, try "help".
"""
doc_header = 'Available commands:'
ruler = '-'
user_creds = []
def emptyline(self):...
def default(self, line):...
if not validate(line):
print('shrub: {}: command not found. Try "help".'.format(line.split(' ', 1)[0])
    )
message = self.send_cmd(line, self.user_creds)
return
print(message)
return
