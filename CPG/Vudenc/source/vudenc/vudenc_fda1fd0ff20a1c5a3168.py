@app.route('/varga')...
varga = request.args.get('varga')
rows = []
con.close()
con.row_factory = sql.Row
cur = con.cursor()
cur.execute("select * from mula where varga = '%s';" % varga)
mula = cur.fetchall()
return render_template('varga.html', mula=mula, varga=varga)
