def setUpClass():...
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
create_test_db()
os.rename(filename, 'temp_' + filename)
for filename in ['cert_db.sqlite3', 'rf_model.pkl', 'rf_features.pkl']:
os.rename('test_' + filename, filename)
