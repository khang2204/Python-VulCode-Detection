def tearDownClass():...
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
os.rename('temp_' + filename, filename)
os.remove(filename)
