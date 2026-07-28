def selection(hint, range):...
index = input(rainbow(hint, color='blue'))
if int(index) > range or int(index) < 0:
print(rainbow('out of range!', color='red'))
return int(index)
selection(hint, range)
