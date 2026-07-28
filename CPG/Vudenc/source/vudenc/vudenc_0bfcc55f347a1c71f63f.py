def get_folder_data(args):...
"""docstring"""
args.inf_file = 'item.inf'
cred_file = args.folderName + '/login.inf'
creds = [line.strip() for line in open(cred_file, 'r')]
args.username = creds[0]
args.password = creds[1]
