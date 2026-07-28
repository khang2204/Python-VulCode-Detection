def run_list_mode(indent='    '):...
"""docstring"""
print('--list: ' + str(args.list))
if args.list == 'a' or args.list == 'all' or args.list == 'g' or args.list == 'groups':
grp = set()
if args.list == 'a' or args.list == 'all' or args.list == 'd' or args.list == 'descriptions':
for s in tweaks.tweaks:
descriptions = set()
grp.add(s['group'])
print('The groups are:')
for d in tweaks.tweaks:
for t in sorted(grp):
descriptions.add(d['group'] + ' | ' + d['description'])
print('group | description:')
print(indent + t)
for t in sorted(descriptions):
print(indent + t)
