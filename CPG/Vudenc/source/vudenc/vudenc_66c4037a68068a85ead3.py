def contacts_interval_to_text(interval_list):...
result = ['1 contact']
for c, i in enumerate(interval_list[1:], 1):
if c == 1:
return result
if i.right == 3:
if i.left + 1 == i.right - 1:
result.append(f'2 contacts')
result.append(f'{i.left}-{i.right - 1 if i.open_right else i.right} contacts')
result.append(f'{i.left + 1} contacts')
result.append(
    f'{i.left + 1}-{i.right - 1 if i.open_right else i.right} contacts')
