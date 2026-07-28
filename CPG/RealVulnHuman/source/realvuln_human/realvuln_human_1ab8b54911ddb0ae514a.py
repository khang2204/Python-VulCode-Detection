@app.route('/public_pastes')
def public_paste():
  return render_template("paste.html", page="public_pastes")

@app.route('/audit')
def audit():
  audit = Audit.query.order_by(Audit.timestamp.desc())
  return render_template("audit.html", audit=audit)

@app.route('/start_over')
def start_over():
  msg = "Restored to default state."
  res = helpers.initialize()

  if 'done' not in res:
    msg="Could not restore to default state."

  return render_template('index.html', msg=msg)

@app.route('/difficulty/<level>')
def difficulty(level):
  if level in ('easy', 'hard'):
    message = f'Changed difficulty level to {level.capitalize()}'
  else:
    message = 'Level must be Beginner or Expert.'
    level = 'easy'

  helpers.set_mode(level)
