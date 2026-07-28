import operator
from collections import deque
def isopen(location):...
x, y = location
num = x * x + 3 * x + 2 * x * y + y + y * y + 1358
return x >= 0 and y >= 0 and bin(num).count('1') % 2 == 0
