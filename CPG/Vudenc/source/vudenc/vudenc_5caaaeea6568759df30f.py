def _regex_sos_help(self, regex, sosinfo, is_list=False):...
res = []
for result in re.findall(regex, sosinfo, re.S):
for line in result.splitlines():
return res
if not is_list:
r = line.split(',')
res.append(line.split()[0])
res.extend(p.strip() for p in r if p.strip())
