def list_to_ordered_str_list(list_of_gadgets):...
string_roaster = ''
index = 1
for item in list_of_gadgets:
if not item[0]:
return string_roaster
string_roaster += '{}. {}\n'.format(index, item[0])
index += 1
