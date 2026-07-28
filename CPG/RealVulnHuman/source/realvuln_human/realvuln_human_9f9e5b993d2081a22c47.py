else:
      result = query

    return result

  def resolve_audits(self, info):
    query = Audit.query.all()
    Audit.create_audit_entry(info)
    return query

  def resolve_delete_all_pastes(self, info):
    Audit.create_audit_entry(info)
    Paste.query.delete()
    db.session.commit()
    return Paste.query.count() == 0


@app.route('/')
def index():
  resp = make_response(render_template('index.html'))
  resp.set_cookie("env", "graphiql:disable")
  return resp

@app.route('/about')
def about():
