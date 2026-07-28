def print_as_a_list_item(index, title, subtile=None):...
index = ('[%s]' % str(index)).center(8).lstrip()
title = print_left_just(rainbow(title, color='green'))
if subtile:
subtile = '\n' + len(index) * ' ' + subtile
subtile = ''
return index + title + subtile
