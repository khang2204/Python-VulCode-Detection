@classmethod
    def create_user(cls, **kw):
      obj = cls(**kw)
      db.session.add(obj)
      db.session.commit()

      return obj


def clean_query(gql_query):
  clean = re.sub(r'(?<=token:")(.*)(?=")', "*****", gql_query)
  clean = re.sub(r'(?<=password:")(.*)(?=")', "*****", clean)
  return clean


class Audit(db.Model):
  __tablename__ = 'audits'
  id = db.Column(db.Integer, primary_key=True)
  gqloperation = db.Column(db.String)
  gqlquery = db.Column(db.String)
  timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

  @classmethod
