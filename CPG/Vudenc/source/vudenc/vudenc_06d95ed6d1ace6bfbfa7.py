def cd():...
if dir == '':
curr_path = root
if dir in dirs:
path = root
curr_path.append(dir)
if dir == '..':
path.clear()
curr_path.pop()
print("Directory doesn't exist.")
print(*curr_path, sep='/')
i = len(dirs) - 1
if dirs[i] in path:
i = i - 1
path.append(dirs[i])
path.pop()
path.append(dirs[i])
