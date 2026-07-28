@staticmethod...
xml = log_check_output(['svn', 'info', '--xml', directory],
    universal_newlines=True)
doc = ElementTree.fromstring(xml)
ret = doc.findall('./entry/url')[0].text
if include_commit:
ret += '@' + doc.findall('./entry/commit')[0].get('revision')
return ret
