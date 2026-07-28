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
confirmed = None
orderComplete = False
multiKeyOrder = False
addMore = None
u_date = datetime.now()
while orderComplete == False:
sys.exit()
clear()
if openConn == True:
while confirmed != 'yes':
db.close()
print('Update the key inventory by entering the order information below.')
confirmed = 'No'
openConn = False
divider()
u_keyNum = int(u_keyNum)
if multiKeyOrder == False:
u_keysUsed = int(u_keysUsed)
u_orderNum = input('Order #: ')
u_keyNum = input('Key used (i.e. #29): #')
print('Connecting to database...')
u_keysUsed = input('# of keys lased: ')
db = pyodbc.connect(Driver='{SQL Server Native Client 11.0}', Server=
    '(LocalDB)\\LocalDB Laser', Database='laserInv', trusted_connection='yes')
clear()
openConn = True
divider()
c1 = db.cursor()
print("""{} 
 Order #: {} 
 Key #: {} 
 # of keys lased: {}""".format(
    u_date, u_orderNum, u_keyNum, u_keysUsed))
c1.execute("SELECT invCount FROM keyInventory WHERE keyNum = '%s';" % u_keyNum)
divider()
u_preCount = c1.fetchall()[0][0]
divider()
u_date = datetime.now()
confirmed = input('Is the information above correct? ')
print(
    "ERROR: The key number you entered doesn't exist in the keyInventory table."
    )
u_postCount = u_preCount - u_keysUsed
if confirmed == 'yes':
print(
    "TIP: If you know you've typed it correctly, you'll have to add it to the Database with newKey.py"
    )
c2 = db.cursor()
clear()
if confirmed == 'no':
divider()
c2.execute(
    'INSERT INTO ordersFilled (submit_time, orderNum, keyNum, keysUsed, preCount, postCount) VALUES (?, ?, ?, ?, ?, ?);'
    , (u_date, u_orderNum, u_keyNum, u_keysUsed, u_preCount, u_postCount))
clear()
clear()
input('Press Enter to close...')
c2.commit()
print('Re-enter the information. \n')
print("Must answer yes or no, it's case sensitive because I'm lazy! \n")
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
sys.exit()
clear()
openConn = False
print('Success! Database has been updated.')
divider()
addMore = None
divider()
while addMore != 'yes' and addMore != 'no':
input('Press Enter to close...')
addMore = input('Are there more keys on this order? ')
if addMore == 'yes':
multiKeyOrder = True
if addMore == 'no':
if openConn == True:
orderComplete = True
clear()
db.close()
print('Okay, bye!')
print("Must answer yes or no, it's case sensitive because I'm lazy!")
openConn = False
