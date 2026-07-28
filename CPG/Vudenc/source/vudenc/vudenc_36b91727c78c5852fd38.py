import cgi
import mysql.connector
from html import beghtml, endhtml
form = cgi.FieldStorage()
insert_table = form.getvalue('insert_table')
values = form.getvalue('values')
if values:
values = values.split(', ')
svalues = ''
if values:
for value in values:
cnx = mysql.connector.connect(user='eapfelba', host='localhost', database=
    'eapfelba2', password='chumash1000')
svalues += "'%s', " % value.strip()
svalues = svalues[:-2]
query = ''
cursor = cnx.cursor()
if insert_table and values:
query = 'insert into %s values (%s)' % (insert_table, svalues)
hasError = False
if not query:
beghtml()
if query:
print("<h3>You didn't fill anything out! :/</h3>")
if hasError == False:
cursor.execute(query)
beghtml()
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>'
    )
beghtml()
cursor.close()
cnx.commit()
print('Something went wrong: {}'.format(err) + '<br><br>')
print(
    '<br><b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Home</a></b>'
    )
print('<h3>')
cnx.close()
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>'
    )
endhtml()
temps = svalues.split(', ')
endhtml()
hasError = True
for s in temps:
hasError = True
print('<b> | %s' % s[1:-1])
print(' | </b></h3>')
print('<h3>is now in the table %s!</h3>' % insert_table)
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/cgi-bin/showdb.py">Current Database</a></b><br><br>'
    )
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>'
    )
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>'
    )
endhtml()
