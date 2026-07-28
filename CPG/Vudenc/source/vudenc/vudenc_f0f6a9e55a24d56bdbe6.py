def print_left_just(output, length=None):...
if length == None:
length = len(output)
return output + (length - len(output)) * ' '
