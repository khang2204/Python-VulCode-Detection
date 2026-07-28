@app.route('/upload', methods=['POST'])...
datafile = request.files['file']
c = MySQL.get_connection(DATABASE)
if datafile:
logfile = os.path.splitext(datafile.filename)[0] + str(int(time.time())
    ) + '.log'
c.close()
f = logging.FileHandler(os.path.join(LOG_DIR, logfile), 'w')
Config.setup_logging(f)
filepath = os.path.join(UPLOADS_DIR, datafile.filename)
datafile.save(filepath)
Importer.run(filepath, c)
logger.removeHandler(f)
f.close()
return jsonify({'name': datafile.filename, 'log': logfile})
