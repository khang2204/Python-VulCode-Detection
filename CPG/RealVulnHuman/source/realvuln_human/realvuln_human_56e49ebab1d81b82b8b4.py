class Login(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    def mutate(self, info , username, password) :
        user = User.query.filter_by(username=username, password=password).first()
        Audit.create_audit_entry(info)
        if not user:
            raise Exception('Authentication Failure')
        return Login(
            access_token = create_access_token(username),
            refresh_token = create_refresh_token(username)
        )

class Mutations(graphene.ObjectType):
  create_paste = CreatePaste.Field()
