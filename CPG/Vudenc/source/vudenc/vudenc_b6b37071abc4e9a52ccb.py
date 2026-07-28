from datetime import datetime
import pyodbc
import sys
import subprocess as sp
from os import system
def clear():...
system('cls')
def divider():...
print('-' * 70)
DBNAME = 'laserInv'
openConn = False
resupplyComplete = False
confirmed = None
addMore = None
while resupplyComplete == False:
sys.exit()
clear()
if openConn == True:
if openConn == True:
print('Update the key inventory by entering the key resupply info below.')
db.close()
divider()
db.close()
divider()
openConn = False
divider()
openConn = False
u_keyNum = input('Key # used (i.e. Key #29): #')
input('Press enter to close...')
u_keysAdded = input('# of keys to add to inventory: ')
sys.exit()
clear()
while confirmed != 'yes':
divider()
confirmed = 'no'
print("""Adding {} key {}'s to the inventory. 
Is this correct?""".format(
    u_keysAdded, u_keyNum))
u_keyNum = int(u_keyNum)
divider()
u_keysAdded = int(u_keysAdded)
confirmed = input('Please enter yes or no: ')
print('Connecting to database...')
if confirmed == 'yes':
db = pyodbc.connect(Driver='{SQL Server Native Client 11.0}', Server=
    '(LocalDB)\\LocalDB Laser', Database=DBNAME, trusted_connection='yes')
clear()
if confirmed == 'no':
openConn = True
clear()
clear()
c1 = db.cursor()
print('Re-enter the information.')
print("Must answer yes or no, it's case sensitive because I'm lazy!")
c1.execute("SELECT invCount FROM keyInventory WHERE keyNum = '%s';" % u_keyNum)
u_keyNum = input('Key # used (i.e. Key #29): #')
u_preCount = c1.fetchall()[0][0]
divider()
u_date = datetime.now()
u_keysAdded = input('# of keys to add to inventory:')
print(
    "ERROR: The key number you entered doesn't exist in the keyInventory table."
    )
u_postCount = u_preCount + u_keysAdded
print(
    "TIP: If you know you've typed it correctly, you'll have to add it to the Database with newKey.py"
    )
c2 = db.cursor()
divider()
c2.execute(
    'INSERT INTO resupply (submit_time, keyNum, keysAdded, preCount, postCount) VALUES (?, ?, ?, ?, ?);'
    , (u_date, u_keyNum, u_keysAdded, u_preCount, u_postCount))
input('Press enter to close...')
c2.commit()
if openConn == True:
c3 = db.cursor()
db.close()
sys.exit()
c3.execute('UPDATE keyInventory SET invCount = ? WHERE keyNum = ?;', (
    u_postCount, u_keyNum))
openConn = False
if openConn == True:
c3.commit()
db.close()
divider()
print('Success! Database has been updated.')
openConn = False
divider()
divider()
input('Press enter to close...')
addMore = None
sys.exit()
while addMore != 'yes' and addMore != 'no':
addMore = input('Would you like to add more keys to the inventory? ')
if addMore == 'yes':
if openConn == True:
if addMore == 'no':
db.close()
resupplyComplete = True
clear()
openConn = False
print('Okay, bye!')
print("Must answer yes or no, it's case sensitive because I'm lazy!")
