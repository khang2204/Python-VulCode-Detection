import cgi
import mysql.connector
from html import beghtml, endhtml
form = cgi.FieldStorage()
search_enzyme = form.getvalue('search_enzyme')
search_process1 = form.getvalue('search_process1')
search_process2 = form.getvalue('search_process2')
search_enzyme2 = form.getvalue('search_enzyme2')
search_process3 = form.getvalue('search_process3')
sub = form.getvalue('sub')
inter = form.getvalue('inter')
search_process5 = form.getvalue('search_process5')
search_enzyme3 = form.getvalue('search_enzyme3')
reac = form.getvalue('reac')
search_enzyme4 = form.getvalue('search_enzyme4')
inter2 = form.getvalue('inter2')
cnx = mysql.connector.connect(user='eapfelba', database='eapfelba2', host=
    'localhost', password='chumash1000')
cursor = cnx.cursor()
query = ''
key = ''
if search_enzyme:
query = ("select process_name from uses where enzyme_name = '%s'" %
    search_enzyme)
if search_process1:
title = 'Processes'
query = ("select enzyme_name from uses where process_name = '%s'" %
    search_process1)
if search_process2:
title = 'Enzymes'
query = (
    "select distinct organelle from uses natural join located_in where process_name = '%s'"
     % search_process2)
if search_enzyme2:
title = 'Organelles'
query = ("select ligand_mechanism from enzyme where enzyme_name = '%s'" %
    search_enzyme2)
if search_process3:
title = 'Ligand Mechanisms'
query = ("select goal_product from process where process_name = '%s'" %
    search_process3)
if sub:
title = 'Goal Products'
query = "select organelle from location where substructure = '%s'" % sub
if inter:
title = 'Organelles'
query = "select concentration from conds where compound = '%s'" % inter
if search_process5:
title = 'Concentrations'
query = (
    "select concentration, compound from operates_under where process_name = '%s'"
     % search_process5)
if search_enzyme3 and reac:
title = 'Conditions'
query = (
    "select product_name from converts where enzyme_name = '%s' and reactant_name = '%s'"
     % (search_enzyme3, reac))
if search_enzyme4:
key = 'one'
title = 'Products'
query = ("select organelle from located_in where enzyme_name = '%s'" %
    search_enzyme4)
if inter2:
title = 'Organelles'
query = (
    "select concenration from intermediate where intermediate_name = '%s'" %
    inter2)
if not query:
title = 'Concentrations'
beghtml()
hasError = False
print("<h3>You didn't fill anything out! :/</h3>")
if query:
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b>'
    )
if hasError == False:
cursor.execute(query)
print('<b>Something went wrong:</b> {}'.format(err) + '<br><br>')
print(
    '<br><b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Home</a></b>'
    )
response = cursor.fetchall()
cursor.close()
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b>'
    )
endhtml()
beghtml()
cnx.close()
endhtml()
if not response:
hasError = True
print('<h3>no results found</h3>')
print('<h3>Results!</h3>')
print('</b><br>')
print('<h3>%s</h3>' % title)
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>'
    )
for r in response:
print(
    '<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b><br><br>'
    )
print('<b> %s' % r[0])
endhtml()
if key:
print('%s</br>' % r[1])
print('<br>')
