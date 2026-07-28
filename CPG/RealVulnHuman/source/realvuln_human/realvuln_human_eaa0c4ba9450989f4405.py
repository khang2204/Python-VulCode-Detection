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

  return render_template('index.html', msg = message)


@app.context_processor
def get_difficulty():
  level = None
  if helpers.is_level_easy():
    level = 'easy'
  else:
    level = 'hard'
  return dict(difficulty=level)
