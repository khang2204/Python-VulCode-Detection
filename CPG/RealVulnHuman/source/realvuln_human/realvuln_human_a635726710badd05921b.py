user_agents = []
  for uas in agents:
    user_agents.append(uas)
  return random.choice(user_agents)

def pump_db():
  print('Populating Database')
  with app.app_context():
    db.create_all()

    admin = User(username="admin", email="admin@blackhatgraphql.com", password=random_password())
    operator = User(username="operator", email="operator@blackhatgraphql.com", password="password123")
    # create tokens for admin & operator

    db.session.add(admin)
    db.session.add(operator)

    owner = Owner(name='DVGAUser')
    db.session.add(owner)

    paste = Paste()
    paste.title = 'Testing Testing'
