def __parse_conf_file(self, conf_file=...
key_val_dict = {}
if conf_file.find('typing-booster:') > 0:
conf_file = conf_file.replace('typing-booster:', '')
comment_patt = re.compile('^#')
for line in file(conf_file):
if not comment_patt.match(line):
return key_val_dict
attr, val = line.strip().split('=', 1)
key_val_dict[attr.strip()] = val.strip()
