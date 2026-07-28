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
import re
from lib.core.data import conf
from lib.core.settings import MATCH_RATIO
def comparison(page, headers=None, getSeqMatcher=False):...
regExpResults = None
if conf.eString and conf.eString in page:
index = page.index(conf.eString)
if conf.eRegexp:
length = len(conf.eString)
regExpResults = re.findall(conf.eRegexp, page, re.I | re.M)
if conf.string:
pageWithoutString = page[:index]
if regExpResults:
if conf.string in page:
if conf.regexp:
pageWithoutString += page[index + length:]
for regExpResult in regExpResults:
return True
return False
if re.search(conf.regexp, page, re.I | re.M):
conf.seqMatcher.set_seq2(page)
page = pageWithoutString
index = page.index(regExpResult)
return True
return False
if getSeqMatcher:
length = len(regExpResult)
return round(conf.seqMatcher.ratio(), 5)
if round(conf.seqMatcher.ratio(), 5) >= MATCH_RATIO:
pageWithoutRegExp = page[:index]
return True
return False
pageWithoutRegExp += page[index + length:]
page = pageWithoutRegExp
