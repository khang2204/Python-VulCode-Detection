def print_right_just(output, length):...
if length == None:
length = len(output)
return (length - len(output)) * ' ' + output
