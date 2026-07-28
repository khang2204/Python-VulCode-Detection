def clean_base(username):...
path = os.path.join(os.path.abspath(os.path.dirname(__file__)) +
    '\\users\\' + username + '.db')
if os.path.exists(path):
os.remove(path)
