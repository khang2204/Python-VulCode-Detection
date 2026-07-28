def check_folders():...
folders = 'data', 'data/database/'
for folder in folders:
if not os.path.exists(folder):
print('Creating ' + folder + ' folder...')
os.makedirs(folder)
