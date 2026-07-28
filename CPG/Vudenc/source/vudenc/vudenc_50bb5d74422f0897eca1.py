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
