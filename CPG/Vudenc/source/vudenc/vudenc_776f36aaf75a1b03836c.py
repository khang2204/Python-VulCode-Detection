def check_files():...
if not os.path.isfile(DATABASE_PATH):
conn = lite.connect(DATABASE_PATH)
c = conn.cursor()
